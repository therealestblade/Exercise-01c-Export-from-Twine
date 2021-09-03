#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"
<html>
  <head>
    <title>Zork</title>
    <script type="text/javascript">
      /**
       * Twison - Twine 2 JSON Export Story Format
       *
       * Copyright (c) 2015 Em Walker
       * https://lazerwalker.com
       *
       * Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
       * associated documentation files (the "Software"), to deal in the Software without restriction,
       * including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
       * and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
       * subject to the following conditions:
       *
       * The above copyright notice and this permission notice shall be included in all copies or substantial
       * portions of the Software.
       *
       * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
       * LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
       * IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
       * WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
       * SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
       */
      var Twison={extractLinksFromText:function(t){var n=t.match(/\[\[.+?\]\]/g);return n?n.map(function(t){var n=t.match(/\[\[(.*?)\-\&gt;(.*?)\]\]/);return n?{name:n[1],link:n[2]}:(t=t.substring(2,t.length-2),{name:t,link:t})}):null},extractPropsFromText:function(t){var n,r={},e=!1;const a=/\{\{((\s|\S)+?)\}\}((\s|\S)+?)\{\{\/\1\}\}/gm;for(;null!==(n=a.exec(t));){const o=n[1],s=n[3].replace(/(\r\n|\n|\r)/gm,""),i=this.extractPropsFromText(s);r[o]=null!==i?i:s,e=!0}return e?r:null},convertPassage:function(t){var n={text:t.innerHTML},r=Twison.extractLinksFromText(n.text);r&&(n.links=r);const e=Twison.extractPropsFromText(n.text);if(e&&(n.props=e),["name","pid","position","tags"].forEach(function(r){var e=t.attributes[r].value;e&&(n[r]=e)}),n.position){var a=n.position.split(",");n.position={x:a[0],y:a[1]}}return n.tags&&(n.tags=n.tags.split(" ")),n},convertStory:function(t){var n=t.getElementsByTagName("tw-passagedata"),r=Array.prototype.slice.call(n).map(Twison.convertPassage),e={passages:r};["name","startnode","creator","creator-version","ifid"].forEach(function(n){var r=t.attributes[n].value;r&&(e[n]=r)});var a={};return e.passages.forEach(function(t){a[t.name]=t.pid}),e.passages.forEach(function(t){t.links&&t.links.forEach(function(t){t.pid=a[t.link],t.pid||(t.broken=!0)})}),e},convert:function(){var t=document.getElementsByTagName("tw-storydata")[0],n=JSON.stringify(Twison.convertStory(t),null,2);document.getElementById("output").innerHTML=n}};window.Twison=Twison;
    </script>
  </head>
  <body>
    <pre id="output"></pre>
    <div id="storyData" style="display: none;">
      <tw-storydata name="Zork" startnode="1" creator="Twine" creator-version="2.3.5" ifid="216ACD94-C70D-42CE-80F1-FA90A0D7F747" zoom="1" format="Twison" format-version="0.0.1" options="" hidden><style role="stylesheet" id="twine-user-stylesheet" type="text/twine-css"></style><script role="script" id="twine-user-script" type="text/twine-javascript"></script><tw-passagedata pid="1" name="West of House" tags="" position="412,189" size="100,100">This is an open field west of a white house, with a boarded front door.

[[NORTH-&gt;North of House]]
[[SOUTH-&gt;South of House]]
[[WEST-&gt;Forest]]</tw-passagedata><tw-passagedata pid="2" name="North of House" tags="" position="262,339" size="100,100">You are facing the north side of a white house. There is no door here, and all the windows are barred.

[[WEST-&gt;West of House]]
[[EAST-&gt;East of House]]
[[NORTH-&gt;Forest]]
</tw-passagedata><tw-passagedata pid="3" name="South of House" tags="" position="412,339" size="100,100">You are facing the south side of a white house. There is no door here, and all the windows are barred.

[[WEST-&gt;West of House]]
[[EAST-&gt;East of House]]
[[SOUTH-&gt;Forest]]</tw-passagedata><tw-passagedata pid="4" name="Forest" tags="" position="562,339" size="100,100">This is a forest, with trees in all directions around you.

[[NORTH-&gt;Sunlit Forest]]
[[EAST-&gt;Forest]]
[[SOUTH-&gt;Forest]]
[[WEST-&gt;Forest]]</tw-passagedata><tw-passagedata pid="5" name="East of House" tags="" position="262,489" size="100,100">You are behind the white house. A path leads into the forest to the east. In one corner of the house there is a small window which is slightly ajar.

[[NORTH-&gt;North of House]]
[[SOUTH-&gt;South of House]]
[[EAST-&gt;Sunlit Forest]]
[[WEST-&gt;Kitchen]]
[[ENTER-&gt;Kitchen]]</tw-passagedata><tw-passagedata pid="6" name="Sunlit Forest" tags="" position="562,489" size="100,100">This is a dimly lit forest, with large trees all around. One particularly large tree with some low branches stands here.

[[NORTH-&gt;Forest]]
[[SOUTH-&gt;Forest]]
[[EAST-&gt;Forest]]
[[WEST-&gt;East of House]]
[[UP-&gt;Tree]]</tw-passagedata><tw-passagedata pid="7" name="Kitchen" tags="" position="262,639" size="100,100">You are in the kitchen of the white house. A table seems to have been used recently for the preparation of food. A passage leads to the west and a dark staircase can be seen leading upward. A dark chimney leads down and to the east is a small window which is open.

[[EAST-&gt;East of House]]</tw-passagedata><tw-passagedata pid="8" name="Tree" tags="" position="562,639" size="100,100">You are about 10 feet above the ground nestled among some large branches. The nearest branch above you is above your reach. Beside you on the branch is a small bird&#39;s nest.

[[DOWN-&gt;Sunlit Forest]]</tw-passagedata></tw-storydata>
    </div>
    <script>
      Twison.convert();
    </script>
  </body>
</html>

world = {}

if "name" in world and "passages" in world:
    print(world["name"])
    print()
    for passage in world["passages"]:
        print(passage["name"])
        print(passage["cleanText"])
        for link in passage["links"]:
            print(link["linkText"])
        print()
