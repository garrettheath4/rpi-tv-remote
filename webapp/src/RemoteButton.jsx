import React, { Component } from 'react';

export default class RemoteButton extends Component {
  constructor(props) {
    super(props);

    // This binding is necessary to make `this` work in the callback
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    console.log("POST " + this.props.url);
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", this.props.url);
    xhttp.send();
  }

  render() {
    return (
      <button type="button" className="btn btn-primary btn-block h-100" onClick={this.handleClick}>
        {this.props.label}
      </button>
    );
  }
}
