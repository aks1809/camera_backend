import fs from 'fs';
import express from 'express';
import { createServer } from 'http';
import { execSync } from 'child_process';

import middlewaresConfig from './config/middleware';
import constants from './config/constants';

const app = express();
const httpServer = createServer(app);

middlewaresConfig(app);

app.get('/capture', (req, res) => {
  execSync('python3 scripts/camera.py');
  const filepath = `/home/user/frinks/camera_backend/images/upload.bmp`;
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
