import React, { Component } from 'react';
import RemoteButton from './RemoteButton'

class App extends Component {
  render() {
    // Raspberry Pi touchscreen resolution is 800 x 480
    return (
      <div style={{height: '480px'}}>
        <div className="container-fluid h-100">
          <div className="row h-50">
            <div className="col-sm-6 p-3">
              <RemoteButton url="/api/source/chromebox" label="Google Hangouts"/>
            </div>
            <div className="col-sm-6 p-3">
              <RemoteButton url="/api/source/rpi" label="News Stream"/>
            </div>
          </div>
          <div className="row h-50">
            <div className="col-sm-6 p-3">
              <RemoteButton url="/api/source/rpi/refresh" label="Refresh News Stream"/>
            </div>
            <div className="col-sm-6 p-3">
              <RemoteButton url="/api/source/rpi/reboot" label="Reboot Raspberry Pi"/>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
