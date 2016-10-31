/*
 * NoGray Slider Component
 *
 * Copyright (c), All right reserved
 * Gazing Design - http://www.NoGray.com
 * http://www.nogray.com/license.php
 */
 
ng.Assets.load_style(ng_config.assets_dir+"components/slider/css/"+ng_config.css_skin_prefix+"slider_style.css");ng.Slider=function(b){this.p=this.create_options(b,{type:"horizontal",start:0,end:100,value:null,values_array:null,range_off:null,css_prefix:"ng_slider_",show_value:true,width:200,height:200,fill:true,step:1,num_thumbs:1,thumb_image:null,slider_image:null,slider_image_disabled:null,values_separator:",",rectangle_separator:":"});this.create_events();if(this.p.disabled){this.p.disabled=false;this.disable.delay(100,this)}this.make_id("slider");this.p.type=this.p.type.toLowerCase();if(ng.defined(this.p.input)){this.set_input(this.p.input)}if(!ng.defined(this.p.value)){if((ng.defined(this.get_input()))&&(this.get_input().value!="")){this.p.value=this.p.input.value.split(this.p.values_separator)}}if((ng.defined(this.p.value))&&(ng.type(this.p.value)!="array")){this.p.value=this.p.value.toString().split(this.p.values_separator)}this.add_event("open",function(){this.reset_elements();this.p.holder_position=this.p.slider_holder.get_position()});this.p.speed=1;this.set_start(this.p.start);this.set_end(this.p.end);this.set_step(this.p.step);this.set_range_off(this.p.range_off,true);if(!ng.defined(this.p.thumb_image)){var a="v_thumb.png";if(this.p.type=="rectangle"){a="r_thumb.png"}else{if(this.p.type=="horizontal"){a="h_thumb.png"}}this.p.thumb_image=ng_config.assets_dir+"components/slider/images/"+a}if(!ng.defined(this.p.slider_image)){var a="v_icon.png";if(this.p.type=="rectangle"){a="r_icon.png"}else{if(this.p.type=="horizontal"){a="h_icon.png"}}this.p.slider_image=ng_config.assets_dir+"components/slider/images/"+a}if(!ng.defined(this.p.slider_image_disabled)){var a="v_icon_disabled.png";if(this.p.type=="rectangle"){a="r_icon_disabled.png"}else{if(this.p.type=="horizontal"){a="h_icon_disabled.png"}}this.p.slider_image_disabled=ng_config.assets_dir+"components/slider/images/"+a}if((ng.defined(this.p.input))||(ng.defined(this.p.object))){this.make()}};ng.Slider.inherit(ng.Component);ng.extend_proto(ng.Slider,{has_type:"slider",make:function(c){if(ng.defined(c)){this.set_input(c)}if(ng.defined(this.p.input)){this.p.input.type="text"}var f=this.p.css_prefix;var e=['<div class="'+f+"holder "+this.p.type+'" id="'+this.id+'_holder" unselectable="on" onselectstart="return false">'];e.push('<div class="'+f+'outer" id="'+this.id+'_outer_div">');e.push('<div class="'+f+'inner" id="'+this.id+'_inner_div">&nbsp;</div>');for(var d=(this.p.num_thumbs-1);d>=0;d--){e.push('<div class="'+f+"fill "+f+"fill_"+(d+1)+'"');if(!this.p.fill){e.push(' style="display:none;" ')}e.push('id="'+this.id+"_fill_"+d+'">&nbsp;</div>')}e.push("</div>");for(var d=0;d<this.p.num_thumbs;d++){e.push('<img src="'+this.p.thumb_image+'" border="0"  id="'+this.id+"_thumb_"+d+'" class="'+f+'thumb" ondragstart="return false;" />')}e.push('<div class="'+f+'value" id="'+this.id+'_value_div"  style="display:none;"></div>');e.push("</div>");this.set_html(e);this.p.slider_holder=ng.get(this.id+"_holder");this.p.value_div=ng.get(this.id+"_value_div");if(this.p.type=="horizontal"){this.set_size(this.p.width)}else{if(this.p.type=="vertical"){this.set_size(null,this.p.height)}else{this.set_size(this.p.width,this.p.height)}}this.p.is_sliding=false;this.p.holder_position=this.p.slider_holder.get_position();this.p.which_thumb=0;this.p.content.style.msTouchAction="none";this.p.content.style.touchAction="none";this.p.content.add_events({mouseenter:function(){if(this.p.show_value){this.p.value_div.set_style("display","")}}.bind(this),mouseleave:function(){this.p.value_div.set_style("display","none")}.bind(this),mousedown:function(h){if(this.is_disabled()){return}this.p.which_thumb=this.get_closest_thumb(h);this.p.holder_position=this.p.slider_holder.get_position();this.p.is_sliding=true;this.fire_event("mousedown",null,h)}.bind(this),mousemove:function(q){if(this.is_disabled()){return}var h=this.p.value;var n=this.get_event_value(q);var j=n[0];var o=n[1];if(o){var m=this.get_value_text(j);if(this.p.type=="rectangle"){m=this.get_value_text([j])}this.p.value_div.set_html(m);if(this.p.is_sliding){var k=this.p.start;if((ng.defined(h))&&(ng.defined(h[this.p.which_thumb]))){k=h[this.p.which_thumb]}for(var l=(this.p.which_thumb-1);l>=0;l--){var p=this.p.start;if((ng.defined(h))&&(ng.defined(h[l]))){p=h[l]}if(this.p.type=="rectangle"){if(((j[0]<=p[0])&&(j[1]<=p[1]))&&((k[0]>=j[0])&&(k[1]>=j[1]))){this.p.which_thumb=l}}else{if((j<=p)&&(k>=j)){this.p.which_thumb=l}}}for(var l=this.p.which_thumb+1;l<this.p.num_thumbs;l++){var p=this.p.start;if((ng.defined(h))&&(ng.defined(h[l]))){p=h[l]}if(this.p.type=="rectangle"){if(((j[0]>=p[0])&&(j[1]>=p[1]))&&((k[0]<=j[0])&&(k[1]<=j[1]))){this.p.which_thumb=l}}else{if((j>=p)&&(k<=j)){this.p.which_thumb=l}}}if(!ng.defined(this.p.value)){this.p.value=[]}this.p.value[this.p.which_thumb]=j;this.reset_value(this.p.value);this.reset_elements();this.fire_event("slide",[j,this.p.which_thumb])}}}.bind(this),mouseup:function(i){if(this.is_disabled()){return}this.p.is_sliding=false;this.p.content.fire_event("mousemove",null,i);var h=this.get_event_value(i);var j=h[0];if(!ng.defined(this.p.value)){this.p.value=[]}this.p.value[this.p.which_thumb]=j;this.set_value(this.p.value);this.fire_event("mouseup",null,i)}.bind(this)});if("ontouchstart" in this.p.content){this.p.content.add_events({touchmove:function(h){this.fire_event("mousemove",null,h)},touchstart:function(h){this.fire_event("mousedown",null,h)},touchend:function(h){this.p.is_sliding=false}.bind(this)})}ng.doc.add_event("mouseup",function(){this.p.is_sliding=false}.bind(this));this.p.content.add_event("mouseup",function(){this.p.is_sliding=false}.bind(this));var a=this.get_input();if(ng.defined(a)){if((!ng.defined(this.p.value))&&(a.value!="")){this.p.value=a.value.split(this.p.values_separator)}a.add_events({change:function(){this.set_value(this.get_input().value)}.bind(this),keyup:function(){this.p.speed=1}.bind(this),keydown:function(j){if(this.p.type=="rectangle"){return}var k=0;if(j.get_key()=="up"){k=1}else{if(j.get_key()=="down"){k=-1}}if(k!=0){var m=this.get_input().value;if((m=="")&&(k==1)){return this.set_value(this.p.start)}if((m=="")&&(k==-1)){return this.set_value(this.p.end)}k=Math.floor(k*this.p.speed);if(m.is_numeric()){m=m.to_int()+(this.p.step*k);if(ng.defined(this.p.range_off)){var h=this.p.range_off;for(var l=0;l<h.length;l++){if((m>=h[l][0])&&(m<=h[l][1])){if(k==-1){m=h[l][0]-1}else{m=h[l][1]+1}break}}}this.set_value(m)}else{if(ng.defined(this.p.values_array)){for(var l=0;l<this.p.values_array.length;l++){if(m==this.p.values_array[l]){this.set_value((l+(this.p.step*k)))}l+=this.p.step-1}}}this.p.speed+=0.1}}.bind(this)});var e=this.get_input_html();ng.hold_html(e);var g=ng.get("input_button_container"+this.id);a.append_element(g,"before");if(ng.defined(ng.UI)){g.append_element(a)}else{ng.get("input_holder_td"+this.id).append_element(a)}this.p.icon_button=new ng.Button({icon:this.p.slider_image,stop_default:true,hide_component:true,language:this.get_language(),color:this.p.buttons_color,over_color:this.p.buttons_over_color,down_color:this.p.buttons_down_color,disable_color:this.p.buttons_disable_color,gloss:this.p.buttons_gloss,checked_color:this.p.buttons_checked_color,light_border:this.p.buttons_light_border,events:{disable:function(){this.p.icon_button.set_icon(this.p.slider_image_disabled)}.bind(this),enable:function(){this.p.icon_button.set_icon(this.p.slider_image)}.bind(this)}});if(ng.defined(ng.UI)){this.p.icon_button.make(g)}else{this.p.icon_button.make("button_holder_td"+this.id)}this.set_button(this.p.icon_button);if(a.disabled){this.disable.delay(100,this)}}if(ng.defined(this.p.value)){this.reset_value(this.p.value)}if(this.get_visible()){var b=new Image();b.onload=(function(){this.reset_elements.defer(this)}.bind(this));b.src=this.p.thumb_image}else{this.reset_elements.defer(this)}return this},get_closest_thumb:function(b){if(this.p.num_thumbs<=1){return 0}var f=this.p.num_thumbs-1;var a=this.p.start;if((ng.defined(this.p.value))&&(ng.defined(this.p.value[f]))){a=this.p.value[f]}var g=this.get_event_value(b);g=g[0];if(this.p.type=="rectangle"){var d=[g[0],g[1]]}else{var d=g}for(var e=0;e<this.p.num_thumbs;e++){var c=this.p.start;if((ng.defined(this.p.value))&&(ng.defined(this.p.value[e]))){c=this.p.value[e]}if(this.p.type=="rectangle"){if((Math.abs(c[0]-d[0])<Math.abs(a[0]-d[0]))&&(Math.abs(c[1]-d[1])<Math.abs(a[1]-d[1]))){a=[c[0],c[1]];f=e}}else{if(Math.abs(c-d)<Math.abs(a-d)){a=c;f=e}}}return f},get_event_value:function(c){var e=c.top-this.p.holder_position.top;var b=c.left-this.p.holder_position.left;if(e<0){e=0}if(e>this.p.height){e=this.p.height}if(b<0){b=0}if(b>this.p.width){b=this.p.width}if(ng.Language.get_dir(this.get_language())=="rtl"){b=Math.abs(b-this.p.width)}e=Math.abs(e-this.p.height);var g=false;if(this.p.type=="rectangle"){b=this.p.end[0].percent((b/this.p.width)*100);if((b%this.p.step[0])>0){b=b-(b%this.p.step[0])}e=this.p.end[1].percent((e/this.p.height)*100);if((e%this.p.step[1])>0){e=e-(e%this.p.step[0])}var f=this.p.start[0];if((ng.defined(this.p.value))&&(ng.defined(this.p.value[this.p.which_thumb]))){f=this.p.value[this.p.which_thumb][0]}if(Math.abs(f-b)>=this.p.step[0]){g=true}f=this.p.start[1];if((ng.defined(this.p.value))&&(ng.defined(this.p.value[this.p.which_thumb]))){f=this.p.value[this.p.which_thumb][1]}if((!g)&&(Math.abs(f-e)>=this.p.step[1])){g=true}f=([b,e])}else{if(this.p.type=="vertical"){e=this.p.end.percent((e/this.p.height)*100);if((e%this.p.step)>0){e=e-(e%this.p.step)}var f=this.p.start;if((ng.defined(this.p.value))&&(ng.defined(this.p.value[this.p.which_thumb]))){f=this.p.value[this.p.which_thumb]}if(Math.abs(f-e)>=this.p.step){g=true}f=e}else{b=this.p.end.percent((b/this.p.width)*100);if((b%this.p.step)>0){b=b-(b%this.p.step)}var f=this.p.start;if((ng.defined(this.p.value))&&(ng.defined(this.p.value[this.p.which_thumb]))){f=this.p.value[this.p.which_thumb]}if(Math.abs(f-b)>=this.p.step){g=true}f=b}}if(ng.defined(this.p.range_off)){var a=this.p.range_off;if(this.p.type=="rectangle"){for(var d=0;d<a.length;d++){if(((f[0]>=a[d][0][0])&&(f[0]<=a[d][0][1]))&&((f[1]>=a[d][1][0])&&(f[1]<=a[d][1][1]))){g=false;break}}}else{for(var d=0;d<a.length;d++){if((f>=a[d][0])&&(f<=a[d][1])){g=false;break}}}}return[f,g]},reset_elements:function(){var b=this.get_end();var h=this.get_start();if(!ng.defined(this.p.thumb_stats)){this.p.thumb_stats={}}for(var c=0;c<this.p.num_thumbs;c++){var g=ng.get(this.id+"_fill_"+c);var e=ng.get(this.id+"_thumb_"+c);if((!ng.defined(this.p.thumb_stats["w"+c]))||(this.p.thumb_stats["w"+c]==0)){this.p.thumb_stats["w"+c]=e.get_width();this.p.thumb_stats["h"+c]=e.get_height();this.p.thumb_stats["flb"+c]=g.get_style("borderLeftWidth").to_int();this.p.thumb_stats["frb"+c]=g.get_style("borderRightWidth").to_int();this.p.thumb_stats["ftb"+c]=g.get_style("borderTopWidth").to_int();this.p.thumb_stats["fbb"+c]=g.get_style("borderBottomWidth").to_int()}var a=this.p.start;if((ng.defined(this.p.value))&&(ng.defined(this.p.value[c]))){a=this.p.value[c]}if(this.p.type=="rectangle"){var k=this.p.width.percent(((a[0]-h[0])/(b[0]-h[0]))*100);var f=this.p.height.percent(((a[1]-h[1])/(b[1]-h[1]))*100)}else{if(!ng.defined(a)){a=h}var k=this.p.width.percent(((a-h)/(b-h))*100);var f=this.p.height.percent(((a-h)/(b-h))*100)}var j={};var d={};if(this.p.type=="rectangle"){j.marginTop=this.p.height-f;j.height=f-this.p.thumb_stats["ftb"+c]-this.p.thumb_stats["fbb"+c];j.width=k-this.p.thumb_stats["flb"+c]-this.p.thumb_stats["frb"+c];d.marginTop=this.p.height-f-Math.round(this.p.thumb_stats["h"+c]/2);if(ng.Language.get_dir(this.get_language())=="ltr"){d.marginLeft=k-Math.round(this.p.thumb_stats["w"+c]/2)}else{d.marginRight=k-Math.round(this.p.thumb_stats["w"+c]/2)}}else{if(this.p.type=="vertical"){j.marginTop=this.p.height-f;j.height=f-this.p.thumb_stats["ftb"+c]-this.p.thumb_stats["fbb"+c];d.marginTop=this.p.height-f-Math.round(this.p.thumb_stats["h"+c]/2)}else{j.width=k-this.p.thumb_stats["flb"+c]-this.p.thumb_stats["frb"+c];if(ng.Language.get_dir(this.get_language())=="ltr"){d.marginLeft=k-Math.round(this.p.thumb_stats["w"+c]/2)}else{d.marginRight=k-Math.round(this.p.thumb_stats["w"+c]/2)}}}e.set_styles(d);g.set_styles(j)}return this},reset_value:function(f){if(f===""){this.p.value=null;this.get_input().value="";return this}if(!ng.defined(this.p.value)){this.p.value=[]}if(ng.type(f)!="array"){f=f.toString().split(this.p.values_separator)}var c=this.p.values_array;if(ng.defined(this.p.range_off)){var b=this.p.range_off}for(var a=0;a<f.length;a++){var g=f[a];if(this.p.type=="rectangle"){if(!ng.defined(g)){g=[this.p.start[0],this.p.start[1]]}if(ng.type(g)!="array"){g=g.toString().split(this.p.rectangle_separator);if(g.length==1){g[1]=g[0]}}if(!g[0].is_numeric()){if(ng.defined(c)){for(var e=0;e<c.length;e++){if(g[0]==c[e][0]){g[0]=e;break}e+=this.p.step-1}}}g[0]=g[0].to_int();if(isNaN(g[0])){g[0]=null}else{g[0]=g[0]-(g[0]%this.p.step[0]);if(g[0]>this.p.end[0]){g[0]=this.p.end[0]}if(g[0]<this.p.start[0]){g[0]=this.p.start[0]}}if(!g[1].is_numeric()){if(ng.defined(c)){for(var e=0;e<c.length;e++){if(g[1]==c[e][1]){g[1]=e;break}e+=this.p.step-1}}}g[1]=g[1].to_int();if(isNaN(g[1])){g[1]=null}else{g[1]=g[1]-(g[1]%this.p.step[1]);if(g[1]>this.p.end[1]){g[1]=this.p.end[1]}if(g[1]<this.p.start[1]){g[1]=this.p.start[1]}}if((b)&&(ng.defined(g))&&(ng.defined(g[0]))&&(ng.defined(g[1]))){for(var e=0;e<b.length;e++){if(((g[0]>=b[e][0][0])&&(g[0]<=b[e][0][1]))&&((g[1]>=b[e][1][0])&&(g[1]<=b[e][1][1]))){var d=(b[e][0][1]-b[e][0][0])/2;if(g[0]>b[e][0][0]+d){g[0]=b[e][0][1]}else{g[0]=b[e][0][0]}d=(b[e][1][1]-b[e][1][0])/2;if(g[1]>b[e][1][0]+d){g[1]=b[e][1][1]}else{g[1]=b[e][1][0]}break}}}}else{if(!ng.defined(g)){g=this.p.start}if(!g.is_numeric()){if(ng.defined(c)){for(var e=0;e<c.length;e++){if(g==c[e]){g=e;break}}}}g=g.to_int();if(isNaN(g)){g=null}else{g=g-(g%this.p.step);if(g>this.p.end){g=this.p.end}if(g<this.p.start){g=this.p.start}if(ng.defined(b)){for(var e=0;e<b.length;e++){if((g>=b[e][0])&&(g<=b[e][1])){var d=(b[e][1]-b[e][0])/2;if(g>b[e][0]+d){g=b[e][1]}else{g=b[e][0]}break}}}}}this.p.value[a]=g}if(ng.defined(this.get_input())){this.get_input().value=this.get_value_text()}return this},set_size:function(a,c){var b={};if(ng.defined(a)){b.width=a}if(ng.defined(c)){b.height=c}ng.get(this.id+"_holder").set_styles(b);ng.get(this.id+"_outer_div").set_styles(b);ng.get(this.id+"_inner_div").set_styles(b);return this.create_out_range()},create_out_range:function(){this.p.slider_holder.get_direct_children("div",function(h){if(h.has_class(this.p.css_prefix+"range_off")){h.remove_element()}}.bind(this));if(ng.defined(this.p.range_off)){var b=this.get_end();var g=this.get_start();var a=this.p.range_off;var d={};for(var f=0;f<a.length;f++){if(this.p.type=="rectangle"){var c=this.p.height.percent(((a[f][1][0]-g[1])/(b[1]-g[1]))*100);d.height=this.p.height.percent(((a[f][1][1]-g[1])/(b[1]-g[1]))*100)-c;d.marginTop=this.p.height-c-d.height;if(ng.Language.get_dir(this.get_language())=="rtl"){var c=d.marginRight=this.p.width.percent(((a[f][0][0]-g[0])/(b[0]-g[0]))*100)}else{var c=d.marginLeft=this.p.width.percent(((a[f][0][0]-g[0])/(b[0]-g[0]))*100)}d.width=this.p.width.percent(((a[f][0][1]-g[0])/(b[0]-g[0]))*100)-c}else{if(this.p.type=="vertical"){var c=this.p.height.percent(((a[f][0]-g)/(b-g))*100);d.height=this.p.height.percent(((a[f][1]-g)/(b-g))*100)-c;d.marginTop=this.p.height-c-d.height}else{if(ng.Language.get_dir(this.get_language())=="rtl"){var c=d.marginRight=this.p.width.percent(((a[f][0]-g)/(b-g))*100)}else{var c=d.marginLeft=this.p.width.percent(((a[f][0]-g)/(b-g))*100)}d.width=this.p.width.percent(((a[f][1]-g)/(b-g))*100)-c}}var e=ng.create("div",{className:this.p.css_prefix+"range_off",html:"&nbsp;",styles:d});this.p.slider_holder.append_element(e)}}},set_width:function(a){this.p.width=a.to_int();if((this.p.type=="horizontal")||(this.p.type=="rectangle")){this.set_size(this.p.width)}return this},get_width:function(){return this.p.width},set_height:function(a){this.p.height=w.to_int();if((this.p.type=="vertical")||(this.p.type=="rectangle")){this.set_size(null,this.p.height)}return this},get_height:function(){return this.p.height},get_value_text:function(d){if(!ng.defined(d)){d=this.get_value()}if(!ng.defined(d)){return""}var a=this.p.values_array;if(ng.type(d)!="array"){d=d.toString().split(this.p.values_separator)}var c=[];for(var b=0;b<d.length;b++){var f=d[b];if(this.p.type=="rectangle"){if(ng.type(f)!="array"){f=f.toString().split(this.p.rectangle_separator)}if(!ng.defined(f[0])){f[0]=this.p.start[0]}if(!ng.defined(f[1])){f[1]=this.p.start[1]}var e=[f[0],f[1]];if(ng.defined(a)){if(ng.defined(a[e[0]])){e[0]=a[e[0]]}if(ng.defined(a[e[1]])){e[1]=a[e[1]]}}c[b]=e.join(this.p.rectangle_separator)}else{if((ng.defined(a))&&(ng.defined(a[f]))){f=a[f]}c[b]=f}}return c.join(this.p.values_separator)},get_value:function(){return this.p.value},set_value:function(a){this.reset_value(a);this.reset_elements();this.fire_event("change");return this},set_start:function(a){if((this.p.type=="rectangle")&&(ng.type(a)!="array")){a=[a,a]}this.p.start=a;return this},get_start:function(){return this.p.start},set_end:function(a){if((this.p.type=="rectangle")&&(ng.type(a)!="array")){a=[a,a]}this.p.end=a;return this},get_end:function(){return this.p.end},set_step:function(a){if((this.p.type=="rectangle")&&(ng.type(a)!="array")){a=[a,a]}this.p.step=a;return this},get_step:function(){return this.p.step},set_range_off:function(b,a){if((ng.defined(b))&&(ng.type(b[0])!="array")){b=[[b[0],b[1]]]}this.p.range_off=b;if(!ng.defined(a)){this.create_out_range()}return this},get_range_off:function(){return this.p.range_off},toString:function(){if(this.p.value.length==0){return""}if(this.p.value.length==1){return this.p.value[0].toString()}return this.p.value.toString()}});ng.map_html5_prop("range",{min:"start",max:"end",step:"step",list:function(d){var c=ng.get(d).getElementsByTagName("OPTION");if(c.length){var a=[];for(var b=0;b<c.length;b++){a.push(c[b].value)}return{values_array:a}}}});if(ng.defined(ng.UI)){ng.UI.add_to_ini("ng-slider",function(a){ng.UI.common_ini(a,ng.Slider)})};