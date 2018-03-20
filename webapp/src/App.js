import React, { Component } from 'react';
import RemoteButton from './RemoteButton'

class App extends Component {
  render() {
    return (
      <div className="container-fluid h-100">
        <div className="row h-50">
          <RemoteButton url="/api/source/chromebox" label="Google Hangouts"/>
          <RemoteButton url="/api/source/rpi" label="News Stream"/>
          <RemoteButton url="/api/test" label="Test 3"/>
          <RemoteButton url="/api/test" label="Test 4"/>
        </div>
        <div className="row h-50">
          <RemoteButton url="/api/test" label="Test 5"/>
          <RemoteButton url="/api/test" label="Test 6"/>
          <RemoteButton url="/api/test" label="Test 7"/>
          <RemoteButton url="/api/test" label="Test 8"/>
        </div>
      </div>
    );
  }
}

export default App;
