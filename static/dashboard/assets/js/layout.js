!function(){"use strict";if(sessionStorage.getItem("defaultAttribute")){for(var e=document.documentElement.attributes,t={},a=0;a<e.length;a++){var s=e[a];s.nodeName&&"undefined"!=s.nodeName&&(t[s.nodeName]=s.nodeValue)}if(JSON.stringify(t)!==sessionStorage.getItem("defaultAttribute"))sessionStorage.clear(),location.reload();else{var o,d={"data-layout":sessionStorage.getItem("data-layout"),"data-sidebar-size":sessionStorage.getItem("data-sidebar-size"),"data-bs-theme":sessionStorage.getItem("data-bs-theme"),"data-layout-width":sessionStorage.getItem("data-layout-width"),"data-sidebar":sessionStorage.getItem("data-sidebar"),"data-sidebar-image":sessionStorage.getItem("data-sidebar-image"),"data-layout-direction":sessionStorage.getItem("data-layout-direction"),"data-layout-style":sessionStorage.getItem("data-layout-style"),"data-topbar":sessionStorage.getItem("data-topbar"),"data-preloader":sessionStorage.getItem("data-preloader")};for(o in d)d[o]&&document.documentElement.setAttribute(o,d[o])}}}();