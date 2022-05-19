import fs from 'fs';
import express from 'express';
import { createServer } from 'http';
import { execSync } from 'child_process';

import middlewaresConfig from './config/middleware';
import constants from './config/constants';

const BASE_PATH = '/home/user/frinks/camera_backend';

const app = express();
const httpServer = createServer(app);

middlewaresConfig(app);

app.get('/capture', async (req, res) => {
  execSync('python3 scripts/camera.py');
  const filepath = `${BASE_PATH}/images/upload.bmp`;
  const imageAsBase64 = fs.readFileSync(filepath, 'base64');
  res.send(imageAsBase64);
});

if (!module.parent) {
  httpServer.listen(constants.PORT, err => {
    if (err) {
      console.log('Cannot run!');
    } else {
      console.log(`API server listening on port: ${constants.PORT}`);
    }
  });
}

export default app;
