(function(t){function e(e){for(var a,c,s=e[0],u=e[1],i=e[2],p=0,h=[];p<s.length;p++)c=s[p],Object.prototype.hasOwnProperty.call(n,c)&&n[c]&&h.push(n[c][0]),n[c]=0;for(a in u)Object.prototype.hasOwnProperty.call(u,a)&&(t[a]=u[a]);l&&l(e);while(h.length)h.shift()();return o.push.apply(o,i||[]),r()}function r(){for(var t,e=0;e<o.length;e++){for(var r=o[e],a=!0,s=1;s<r.length;s++){var u=r[s];0!==n[u]&&(a=!1)}a&&(o.splice(e--,1),t=c(c.s=r[0]))}return t}var a={},n={index:0},o=[];function c(e){if(a[e])return a[e].exports;var r=a[e]={i:e,l:!1,exports:{}};return t[e].call(r.exports,r,r.exports,c),r.l=!0,r.exports}c.m=t,c.c=a,c.d=function(t,e,r){c.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:r})},c.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},c.t=function(t,e){if(1&e&&(t=c(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var r=Object.create(null);if(c.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var a in t)c.d(r,a,function(e){return t[e]}.bind(null,a));return r},c.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return c.d(e,"a",e),e},c.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},c.p="/static/vue/";var s=window["webpackJsonp"]=window["webpackJsonp"]||[],u=s.push.bind(s);s.push=e,s=s.slice();for(var i=0;i<s.length;i++)e(s[i]);var l=u;o.push([0,"chunk-vendors"]),r()})({0:function(t,e,r){t.exports=r("56d7")},"56d7":function(t,e,r){"use strict";r.r(e);r("e260"),r("e6cf"),r("cca6"),r("a79d");var a=r("7a23"),n=Object(a["d"])("h1",null,"Query FAIRVASC Registry",-1),o={id:"get_data_table"},c={class:"get"},s=Object(a["d"])("tr",null,[Object(a["d"])("th",{class:"get"},[Object(a["d"])("h3",null,"Select Endpoint")]),Object(a["d"])("th",{class:"get"},[Object(a["d"])("h3",null,"Select Query Type")]),Object(a["d"])("th",{class:"get"},[Object(a["d"])("h3",null,"Select Query Parameter")])],-1),u=Object(a["d"])("td",{class:"get"}," placeholder ",-1),i={class:"get"},l={class:"form_select",id:"query_select"},p=Object(a["d"])("td",{class:"get"}," placeholder ",-1),h=Object(a["d"])("p",null,null,-1),d={id:"results"},f={class:"vis"},_=Object(a["d"])("td",{class:"vis"},"test",-1),b={class:"vis"};function y(t,e,r,y,g,m){var j=Object(a["g"])("FormSelect"),v=Object(a["g"])("BarChart");return Object(a["e"])(),Object(a["c"])(a["a"],null,[n,Object(a["d"])("div",o,[Object(a["d"])("table",c,[s,Object(a["d"])("tr",null,[u,Object(a["d"])("td",i,[Object(a["d"])("div",l,[Object(a["d"])(j,{options:t.type_options,onChange:e[1]||(e[1]=function(t){return m.chooseParams()}),modelValue:t.query_type,"onUpdate:modelValue":e[2]||(e[2]=function(e){return t.query_type=e})},null,8,["options","modelValue"])])]),p])])]),h,Object(a["d"])("h2",null,Object(a["h"])(t.registry)+": "+Object(a["h"])(t.query_type_long)+": "+Object(a["h"])(t.query_param_long),1),Object(a["d"])("div",d,[Object(a["d"])("table",f,[Object(a["d"])("tr",null,[_,Object(a["d"])("td",b,[Object(a["d"])(v,{class:"chart"})])])])])],64)}var g=r("1da1"),m=(r("96cf"),r("5319"),r("ac1f"),r("caad"),r("2532"),r("d3b7"),r("25f0"),r("bc3a")),j=r.n(m),v=(r("99af"),Object(a["d"])("line",{stroke:"currentColor",y2:"6"},null,-1)),O={fill:"currentColor",y:"9",dy:"0.71em"},w=Object(a["d"])("line",{stroke:"currentColor",x2:"-6"},null,-1),x={fill:"currentColor",x:"-9",dy:"0.32em"},q={class:"bars",fill:"none"};function k(t,e,r,n,o,c){return Object(a["e"])(),Object(a["c"])("svg",{class:"barchart",width:r.width+r.marginLeft/2,height:r.height+r.marginTop},[Object(a["d"])("g",{transform:"translate(".concat(r.marginLeft/2,", ").concat(r.marginTop/2,")")},[Object(a["d"])("g",{class:"x-axis",fill:"none",transform:"translate(0, ".concat(r.height,")"),style:{color:"#888"}},[Object(a["d"])("path",{class:"domain",stroke:"currentColor",d:"M0.5,6V0.5H".concat(r.width,".5V6")},null,8,["d"]),(Object(a["e"])(!0),Object(a["c"])(a["a"],null,Object(a["f"])(c.bars,(function(t,e){return Object(a["e"])(),Object(a["c"])("g",{class:"tick",opacity:"1","font-size":"10","font-family":"sans-serif","text-anchor":"middle",key:e,transform:"translate(".concat(t.x+t.width/2,", 0)")},[v,Object(a["d"])("text",O,Object(a["h"])(t.xLabel),1)],8,["transform"])})),128))],8,["transform"]),Object(a["d"])("g",{class:"y-axis",fill:"none",transform:"translate(0, 0)",style:{color:"#888"}},[Object(a["d"])("path",{class:"domain",stroke:"currentColor",d:"M0.5,".concat(r.height,".5H0.5V0.5H-6")},null,8,["d"]),(Object(a["e"])(!0),Object(a["c"])(a["a"],null,Object(a["f"])(c.yTicks,(function(t,e){return Object(a["e"])(),Object(a["c"])("g",{class:"tick",opacity:"1","font-size":"10","font-family":"sans-serif","text-anchor":"end",key:e,transform:"translate(0, ".concat(c.y(t)+.5,")")},[w,Object(a["d"])("text",x,Object(a["h"])(t),1)],8,["transform"])})),128))],8,["transform"]),Object(a["d"])("g",q,[(Object(a["e"])(!0),Object(a["c"])(a["a"],null,Object(a["f"])(c.bars,(function(t,e){return Object(a["e"])(),Object(a["c"])("rect",{fill:"#2196f3",key:e,height:t.height,width:t.width,x:t.x,y:t.y},null,8,["height","width","x","y"])})),128))])],8,["transform"])],8,["width","height"])}var S=r("2909"),R=(r("d81d"),r("d53d")),C=r("6510"),D={name:"BarChart",props:{height:{default:200},width:{default:500},dataSet:{default:[["Bob",33],["Robin",24],["Mark",22],["Joe",29],["Eve",38],["Karen",21],["Kirsty",25],["Chris",30]]},marginLeft:{default:40},marginTop:{default:40},marginBottom:{default:40},marginRight:{default:40},tickCount:{default:5},barPadding:{default:.3}},computed:{yTicks:function(){return this.y.ticks(this.tickCount)},x:function(){return Object(R["a"])().range([0,this.width]).padding(this.barPadding).domain(this.dataSet.map((function(t){return t[0]})))},y:function(){var t=this.dataSet.map((function(t){return t[1]}));return Object(C["a"])().range([this.height,0]).domain([0,Math.max.apply(Math,Object(S["a"])(t))])},bars:function(){var t=this,e=this.dataSet.map((function(e){return{xLabel:e[0],x:t.x(e[0]),y:t.y(e[1]),width:t.x.bandwidth(),height:t.height-t.y(e[1])}}));return e}}};D.render=k;var P=D;function M(t,e,r,n,o,c){return Object(a["j"])((Object(a["e"])(),Object(a["c"])("select",{"onUpdate:modelValue":e[1]||(e[1]=function(t){return o.selected=t})},[(Object(a["e"])(!0),Object(a["c"])(a["a"],null,Object(a["f"])(r.options,(function(t){return Object(a["e"])(),Object(a["c"])("option",{value:t.value,key:t.value},Object(a["h"])(t.text),9,["value"])})),128))],512)),[[a["i"],o.selected]])}var T={data:function(){return{selected:""}},props:["options"]};T.render=M;var V=T,Q={name:"app",el:"#app",components:{BarChart:P,FormSelect:V},data:function(){return{registry_options:["Hoth"],registry:"Registry",type_options:[{value:"count",text:"Total Patient Count"},{value:"ancaSpecDeath",text:"Deaths by ANCA Specificity"},{value:"sexDeath",text:"Deaths by Sex"},{value:"diagDeath",text:"Deaths by Main Diagnosis"},{value:"ancaIFDeath",text:"Deaths by ANCA IF"}],param_options:[],query_type:"",query_type_long:"Query Results",query_param:"",query_param_long:"",results_table:[]}},methods:{reset:function(){var t=this;t.query_type="",t.query_type_long="Query Results",t.query_param="",t.query_param_long="",t.results_table=[]},chooseParams:function(){var t=Object(g["a"])(regeneratorRuntime.mark((function t(){var e,r,a,n,o;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:for(r in e=this,console.log("chooseParams triggered:",e.query_type),e.type_options)a=e.type_options[r],a.value===e.query_type&&(e.query_type_long=a.text);e.results_table=[],"count"===e.query_type?(e.getCount(),console.log("count")):(n=e.query_type.replace("Death",""),o="/sparql/getQueryParameters".concat("?stratify_type="+n),j.a.get(o,{stratify_type:n}).then(function(){var t=Object(g["a"])(regeneratorRuntime.mark((function t(r){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:if(!r.ok){t.next=7;break}return t.next=3,r.json();case 3:e.param_options=t.sent,console.log("options:",e.param_options),t.next=8;break;case 7:e.results_table=[{error:r}];case 8:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}()));case 5:case"end":return t.stop()}}),t,this)})));function e(){return t.apply(this,arguments)}return e}(),callQuery:function(){var t=Object(g["a"])(regeneratorRuntime.mark((function t(){var e,r;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:for(e in this.param_options)r=this.param_options[e],r.value===this.query_param&&(this.query_param_long=r.text);if(""!==this.query_param){t.next=5;break}return t.abrupt("return");case 5:this.query_type.includes("Death")&&this.getDeathCountSingle();case 6:case"end":return t.stop()}}),t,this)})));function e(){return t.apply(this,arguments)}return e}(),getCount:function(){var t=Object(g["a"])(regeneratorRuntime.mark((function t(){var e;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:e=this,e.param_options=[],e.query_param="",e.query_param_long="",fetch("/sparql/get_total_count",(function(){})).then(function(){var t=Object(g["a"])(regeneratorRuntime.mark((function t(r){var a;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,r.json();case 2:a=t.sent,e.results_table=[{parameter:e.query_type_long,value:a.total_count}];case 4:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}()).catch((function(t){console.error(t),e.results_table=[{error:t}]}));case 5:case"end":return t.stop()}}),t,this)})));function e(){return t.apply(this,arguments)}return e}(),getDeathCountSingle:function(){var t=Object(g["a"])(regeneratorRuntime.mark((function t(){var e,r,a;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:e=this,r=this.query_type.replace("Death",""),a="/sparql/get_death_count_single".concat("?stratify_type=",r,"&stratify_param=",this.query_param),fetch(a,(function(){})).then(function(){var t=Object(g["a"])(regeneratorRuntime.mark((function t(r){var a,n;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,r.json();case 2:a=t.sent,n={raw_strat_deaths:a.strat_death_count,strat_death_of_all_strat:A(a.strat_death_count,a.total_strat_count),strat_death_of_all_death:A(a.strat_death_count,a.total_death_count),strat_alive_of_all_alive:A(a.total_strat_count,a.total_count)},e.visualiseSingleStratDeath(n);case 5:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}()).catch((function(t){console.error(t),e.results_table=[{error:t}]}));case 4:case"end":return t.stop()}}),t,this)})));function e(){return t.apply(this,arguments)}return e}(),visualiseSingleStratDeath:function(){var t=Object(g["a"])(regeneratorRuntime.mark((function t(e){var r;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:r=this,"sexDeath"===r.query_type?(r.results_table=[{parameter:"number of deaths of "+r.query_param_long+" patients",value:e.raw_strat_deaths},{parameter:"% of "+r.query_param_long+" patients who have died",value:e.strat_death_of_all_strat.toString()+"%"},{parameter:"% of deceased patients who were "+r.query_param_long,value:e.strat_death_of_all_death.toString()+"%"},{parameter:"% of living patients who were "+r.query_param_long,value:e.strat_alive_of_all_alive.toString()+"%"}],console.log(r.results_table)):r.results_table=[{parameter:'number of deaths of patients with "'+r.query_param_long+'"',value:e.raw_strat_deaths},{parameter:'% of "'+r.query_param_long+'" patients who have died',value:e.strat_death_of_all_strat.toString()+"%"},{parameter:'% of deceased patients who had "'+r.query_param_long+'"',value:e.strat_death_of_all_death.toString()+"%"},{parameter:'% of living patients who have "'+r.query_param_long+'"',value:e.strat_alive_of_all_alive.toString()+"%"}];case 2:case"end":return t.stop()}}),t,this)})));function e(e){return t.apply(this,arguments)}return e}()}};function A(t,e){var r=0;return 0!=e&&0!=t&&(r=Math.round(100*t/e)),r}r("889c");Q.render=y;var B=Q;Object(a["b"])(B).mount("#app")},"889c":function(t,e,r){"use strict";r("e1ec")},e1ec:function(t,e,r){}});
//# sourceMappingURL=index.53cffbb5.js.map