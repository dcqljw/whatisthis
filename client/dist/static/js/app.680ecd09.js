(function(e){function n(n){for(var r,i,a=n[0],c=n[1],s=n[2],l=0,p=[];l<a.length;l++)i=a[l],Object.prototype.hasOwnProperty.call(o,i)&&o[i]&&p.push(o[i][0]),o[i]=0;for(r in c)Object.prototype.hasOwnProperty.call(c,r)&&(e[r]=c[r]);f&&f(n);while(p.length)p.shift()();return u.push.apply(u,s||[]),t()}function t(){for(var e,n=0;n<u.length;n++){for(var t=u[n],r=!0,i=1;i<t.length;i++){var c=t[i];0!==o[c]&&(r=!1)}r&&(u.splice(n--,1),e=a(a.s=t[0]))}return e}var r={},o={app:0},u=[];function i(e){return a.p+"static/js/"+({}[e]||e)+"."+{"chunk-2d0c4856":"dd4305a9","chunk-2d21e30b":"e12e1e03"}[e]+".js"}function a(n){if(r[n])return r[n].exports;var t=r[n]={i:n,l:!1,exports:{}};return e[n].call(t.exports,t,t.exports,a),t.l=!0,t.exports}a.e=function(e){var n=[],t=o[e];if(0!==t)if(t)n.push(t[2]);else{var r=new Promise((function(n,r){t=o[e]=[n,r]}));n.push(t[2]=r);var u,c=document.createElement("script");c.charset="utf-8",c.timeout=120,a.nc&&c.setAttribute("nonce",a.nc),c.src=i(e);var s=new Error;u=function(n){c.onerror=c.onload=null,clearTimeout(l);var t=o[e];if(0!==t){if(t){var r=n&&("load"===n.type?"missing":n.type),u=n&&n.target&&n.target.src;s.message="Loading chunk "+e+" failed.\n("+r+": "+u+")",s.name="ChunkLoadError",s.type=r,s.request=u,t[1](s)}o[e]=void 0}};var l=setTimeout((function(){u({type:"timeout",target:c})}),12e4);c.onerror=c.onload=u,document.head.appendChild(c)}return Promise.all(n)},a.m=e,a.c=r,a.d=function(e,n,t){a.o(e,n)||Object.defineProperty(e,n,{enumerable:!0,get:t})},a.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},a.t=function(e,n){if(1&n&&(e=a(e)),8&n)return e;if(4&n&&"object"===typeof e&&e&&e.__esModule)return e;var t=Object.create(null);if(a.r(t),Object.defineProperty(t,"default",{enumerable:!0,value:e}),2&n&&"string"!=typeof e)for(var r in e)a.d(t,r,function(n){return e[n]}.bind(null,r));return t},a.n=function(e){var n=e&&e.__esModule?function(){return e["default"]}:function(){return e};return a.d(n,"a",n),n},a.o=function(e,n){return Object.prototype.hasOwnProperty.call(e,n)},a.p="",a.oe=function(e){throw console.error(e),e};var c=window["webpackJsonp"]=window["webpackJsonp"]||[],s=c.push.bind(c);c.push=n,c=c.slice();for(var l=0;l<c.length;l++)n(c[l]);var f=s;u.push([0,"chunk-vendors"]),t()})({0:function(e,n,t){e.exports=t("56d7")},"034f":function(e,n,t){"use strict";t("85ec")},"56d7":function(e,n,t){"use strict";t.r(n);t("e260"),t("e6cf"),t("cca6"),t("a79d");var r=t("2b0e"),o=(t("d3b7"),t("bc3a")),u=t.n(o),i={},a=u.a.create(i);a.interceptors.request.use((function(e){return e}),(function(e){return Promise.reject(e)})),a.interceptors.response.use((function(e){return e}),(function(e){return Promise.reject(e)})),Plugin.install=function(e,n){e.axios=a,window.axios=a,Object.defineProperties(e.prototype,{axios:{get:function(){return a}},$axios:{get:function(){return a}}})},r["default"].use(Plugin);Plugin;var c=function(){var e=this,n=e.$createElement,t=e._self._c||n;return t("div",{attrs:{id:"app"}},[t("router-view")],1)},s=[],l={name:"app"},f=l,p=(t("034f"),t("2877")),d=Object(p["a"])(f,c,s,!1,null,null,null),h=d.exports,b=(t("3ca3"),t("ddb0"),t("8c4f"));r["default"].use(b["a"]);var v=[{path:"/",name:"index",component:function(){return t.e("chunk-2d21e30b").then(t.bind(null,"d504"))}},{path:"/xby",name:"article",component:function(){return t.e("chunk-2d0c4856").then(t.bind(null,"3ad6"))}}],m=new b["a"]({mode:"hash",routes:v}),y=m,g=t("5c96"),w=t.n(g);t("0fae");r["default"].use(w.a);var j="https://api.dlxz.xyz";u.a.defaults.baseURL=j,r["default"].config.productionTip=!1,new r["default"]({router:y,render:function(e){return e(h)}}).$mount("#app")},"85ec":function(e,n,t){}});
//# sourceMappingURL=app.680ecd09.js.map