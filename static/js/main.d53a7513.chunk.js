(this.webpackJsonpwebapp=this.webpackJsonpwebapp||[]).push([[0],{13:function(e,n,t){},14:function(e,n,t){"use strict";t.r(n);var o=t(0),a=t.n(o),r=t(7),i=t.n(r),c=(t(13),t(1)),l=t(2),s=t(5),u=t(4),p=t(3),h=function(e){Object(s.a)(t,e);var n=Object(u.a)(t);function t(e){var o;return Object(c.a)(this,t),(o=n.call(this,e)).handleClick=o.handleClick.bind(Object(p.a)(o)),o}return Object(l.a)(t,[{key:"handleClick",value:function(){console.log("POST "+this.props.url);var e=new XMLHttpRequest;e.open("POST",this.props.url),e.send()}},{key:"render",value:function(){return a.a.createElement("button",{type:"button",className:"btn btn-primary btn-block h-100",onClick:this.handleClick},a.a.createElement("h3",null,this.props.label))}}]),t}(o.Component),m=function(e){Object(s.a)(t,e);var n=Object(u.a)(t);function t(){return Object(c.a)(this,t),n.apply(this,arguments)}return Object(l.a)(t,[{key:"render",value:function(){return a.a.createElement("div",{style:{height:"480px"}},a.a.createElement("div",{className:"container-fluid h-100"},a.a.createElement("div",{className:"row h-50"},a.a.createElement("div",{className:"col-sm-6 p-3"},a.a.createElement(h,{url:"/api/source/chromecast",label:"Chromecast"})),a.a.createElement("div",{className:"col-sm-6 p-3"},a.a.createElement(h,{url:"/api/source/rpi",label:"News Stream"}))),a.a.createElement("div",{className:"row h-50"},a.a.createElement("div",{className:"col-sm-6 p-3"},a.a.createElement(h,{url:"/api/source/rpi/refresh",label:"Refresh News Stream"})),a.a.createElement("div",{className:"col-sm-6 p-3"},a.a.createElement(h,{url:"/api/source/rpi/reboot",label:"Reboot Raspberry Pi"})))))}}]),t}(o.Component),d=Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));function f(e){navigator.serviceWorker.register(e).then((function(e){e.onupdatefound=function(){var n=e.installing;n.onstatechange=function(){"installed"===n.state&&(navigator.serviceWorker.controller?console.log("New content is available; please refresh."):console.log("Content is cached for offline use."))}}})).catch((function(e){console.error("Error during service worker registration:",e)}))}i.a.render(a.a.createElement(m,null),document.getElementById("root")),function(){if("serviceWorker"in navigator){if(new URL("/rpi-tv-remote",window.location).origin!==window.location.origin)return;window.addEventListener("load",(function(){var e="".concat("/rpi-tv-remote","/service-worker.js");d?(!function(e){fetch(e).then((function(n){404===n.status||-1===n.headers.get("content-type").indexOf("javascript")?navigator.serviceWorker.ready.then((function(e){e.unregister().then((function(){window.location.reload()}))})):f(e)})).catch((function(){console.log("No internet connection found. App is running in offline mode.")}))}(e),navigator.serviceWorker.ready.then((function(){console.log("This web app is being served cache-first by a service worker. To learn more, visit https://goo.gl/SC7cgQ")}))):f(e)}))}}()},8:function(e,n,t){e.exports=t(14)}},[[8,1,2]]]);
//# sourceMappingURL=main.d53a7513.chunk.js.map