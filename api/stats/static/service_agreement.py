data = """
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>서비스 이용약관</title><style>
/* cspell:disable-file */
/* webkit printing magic: print all background colors */
html {
	-webkit-print-color-adjust: exact;
}
* {
	box-sizing: border-box;
	-webkit-print-color-adjust: exact;
}

html,
body {
	margin: 0;
	padding: 0;
}
@media only screen {
	body {
		margin: 2em auto;
		max-width: 900px;
		color: rgb(55, 53, 47);
	}
}

body {
	line-height: 1.5;
	white-space: pre-wrap;
}

a,
a.visited {
	color: inherit;
	text-decoration: underline;
}

.pdf-relative-link-path {
	font-size: 80%;
	color: #444;
}

h1,
h2,
h3 {
	letter-spacing: -0.01em;
	line-height: 1.2;
	font-weight: 600;
	margin-bottom: 0;
}

.page-title {
	font-size: 2.5rem;
	font-weight: 700;
	margin-top: 0;
	margin-bottom: 0.75em;
}

h1 {
	font-size: 1.875rem;
	margin-top: 1.875rem;
}

h2 {
	font-size: 1.5rem;
	margin-top: 1.5rem;
}

h3 {
	font-size: 1.25rem;
	margin-top: 1.25rem;
}

.source {
	border: 1px solid #ddd;
	border-radius: 3px;
	padding: 1.5em;
	word-break: break-all;
}

.callout {
	border-radius: 3px;
	padding: 1rem;
}

figure {
	margin: 1.25em 0;
	page-break-inside: avoid;
}

figcaption {
	opacity: 0.5;
	font-size: 85%;
	margin-top: 0.5em;
}

mark {
	background-color: transparent;
}

.indented {
	padding-left: 1.5em;
}

hr {
	background: transparent;
	display: block;
	width: 100%;
	height: 1px;
	visibility: visible;
	border: none;
	border-bottom: 1px solid rgba(55, 53, 47, 0.09);
}

img {
	max-width: 100%;
}

@media only print {
	img {
		max-height: 100vh;
		object-fit: contain;
	}
}

@page {
	margin: 1in;
}

.collection-content {
	font-size: 0.875rem;
}

.column-list {
	display: flex;
	justify-content: space-between;
}

.column {
	padding: 0 1em;
}

.column:first-child {
	padding-left: 0;
}

.column:last-child {
	padding-right: 0;
}

.table_of_contents-item {
	display: block;
	font-size: 0.875rem;
	line-height: 1.3;
	padding: 0.125rem;
}

.table_of_contents-indent-1 {
	margin-left: 1.5rem;
}

.table_of_contents-indent-2 {
	margin-left: 3rem;
}

.table_of_contents-indent-3 {
	margin-left: 4.5rem;
}

.table_of_contents-link {
	text-decoration: none;
	opacity: 0.7;
	border-bottom: 1px solid rgba(55, 53, 47, 0.18);
}

table,
th,
td {
	border: 1px solid rgba(55, 53, 47, 0.09);
	border-collapse: collapse;
}

table {
	border-left: none;
	border-right: none;
}

th,
td {
	font-weight: normal;
	padding: 0.25em 0.5em;
	line-height: 1.5;
	min-height: 1.5em;
	text-align: left;
}

th {
	color: rgba(55, 53, 47, 0.6);
}

ol,
ul {
	margin: 0;
	margin-block-start: 0.6em;
	margin-block-end: 0.6em;
}

li > ol:first-child,
li > ul:first-child {
	margin-block-start: 0.6em;
}

ul > li {
	list-style: disc;
}

ul.to-do-list {
	padding-inline-start: 0;
}

ul.to-do-list > li {
	list-style: none;
}

.to-do-children-checked {
	text-decoration: line-through;
	opacity: 0.375;
}

ul.toggle > li {
	list-style: none;
}

ul {
	padding-inline-start: 1.7em;
}

ul > li {
	padding-left: 0.1em;
}

ol {
	padding-inline-start: 1.6em;
}

ol > li {
	padding-left: 0.2em;
}

.mono ol {
	padding-inline-start: 2em;
}

.mono ol > li {
	text-indent: -0.4em;
}

.toggle {
	padding-inline-start: 0em;
	list-style-type: none;
}

/* Indent toggle children */
.toggle > li > details {
	padding-left: 1.7em;
}

.toggle > li > details > summary {
	margin-left: -1.1em;
}

.selected-value {
	display: inline-block;
	padding: 0 0.5em;
	background: rgba(206, 205, 202, 0.5);
	border-radius: 3px;
	margin-right: 0.5em;
	margin-top: 0.3em;
	margin-bottom: 0.3em;
	white-space: nowrap;
}

.collection-title {
	display: inline-block;
	margin-right: 1em;
}

.page-description {
    margin-bottom: 2em;
}

.simple-table {
	margin-top: 1em;
	font-size: 0.875rem;
	empty-cells: show;
}
.simple-table td {
	height: 29px;
	min-width: 120px;
}

.simple-table th {
	height: 29px;
	min-width: 120px;
}

.simple-table-header-color {
	background: rgb(247, 246, 243);
	color: black;
}
.simple-table-header {
	font-weight: 500;
}

time {
	opacity: 0.5;
}

.icon {
	display: inline-block;
	max-width: 1.2em;
	max-height: 1.2em;
	text-decoration: none;
	vertical-align: text-bottom;
	margin-right: 0.5em;
}

img.icon {
	border-radius: 3px;
}

.user-icon {
	width: 1.5em;
	height: 1.5em;
	border-radius: 100%;
	margin-right: 0.5rem;
}

.user-icon-inner {
	font-size: 0.8em;
}

.text-icon {
	border: 1px solid #000;
	text-align: center;
}

.page-cover-image {
	display: block;
	object-fit: cover;
	width: 100%;
	max-height: 30vh;
}

.page-header-icon {
	font-size: 3rem;
	margin-bottom: 1rem;
}

.page-header-icon-with-cover {
	margin-top: -0.72em;
	margin-left: 0.07em;
}

.page-header-icon img {
	border-radius: 3px;
}

.link-to-page {
	margin: 1em 0;
	padding: 0;
	border: none;
	font-weight: 500;
}

p > .user {
	opacity: 0.5;
}

td > .user,
td > time {
	white-space: nowrap;
}

input[type="checkbox"] {
	transform: scale(1.5);
	margin-right: 0.6em;
	vertical-align: middle;
}

p {
	margin-top: 0.5em;
	margin-bottom: 0.5em;
}

.image {
	border: none;
	margin: 1.5em 0;
	padding: 0;
	border-radius: 0;
	text-align: center;
}

.code,
code {
	background: rgba(135, 131, 120, 0.15);
	border-radius: 3px;
	padding: 0.2em 0.4em;
	border-radius: 3px;
	font-size: 85%;
	tab-size: 2;
}

code {
	color: #eb5757;
}

.code {
	padding: 1.5em 1em;
}

.code-wrap {
	white-space: pre-wrap;
	word-break: break-all;
}

.code > code {
	background: none;
	padding: 0;
	font-size: 100%;
	color: inherit;
}

blockquote {
	font-size: 1.25em;
	margin: 1em 0;
	padding-left: 1em;
	border-left: 3px solid rgb(55, 53, 47);
}

.bookmark {
	text-decoration: none;
	max-height: 8em;
	padding: 0;
	display: flex;
	width: 100%;
	align-items: stretch;
}

.bookmark-title {
	font-size: 0.85em;
	overflow: hidden;
	text-overflow: ellipsis;
	height: 1.75em;
	white-space: nowrap;
}

.bookmark-text {
	display: flex;
	flex-direction: column;
}

.bookmark-info {
	flex: 4 1 180px;
	padding: 12px 14px 14px;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
}

.bookmark-image {
	width: 33%;
	flex: 1 1 180px;
	display: block;
	position: relative;
	object-fit: cover;
	border-radius: 1px;
}

.bookmark-description {
	color: rgba(55, 53, 47, 0.6);
	font-size: 0.75em;
	overflow: hidden;
	max-height: 4.5em;
	word-break: break-word;
}

.bookmark-href {
	font-size: 0.75em;
	margin-top: 0.25em;
}

.sans { font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI Variable Display", "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol"; }
.code { font-family: "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace; }
.serif { font-family: Lyon-Text, Georgia, ui-serif, serif; }
.mono { font-family: iawriter-mono, Nitti, Menlo, Courier, monospace; }
.pdf .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI Variable Display", "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK JP'; }
.pdf:lang(zh-CN) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI Variable Display", "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK SC'; }
.pdf:lang(zh-TW) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI Variable Display", "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK TC'; }
.pdf:lang(ko-KR) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI Variable Display", "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK KR'; }
.pdf .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; }
.pdf:lang(zh-CN) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; }
.pdf:lang(zh-TW) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; }
.pdf:lang(ko-KR) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; }
.pdf .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK JP'; }
.pdf:lang(zh-CN) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK SC'; }
.pdf:lang(zh-TW) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK TC'; }
.pdf:lang(ko-KR) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK KR'; }
.pdf .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; }
.pdf:lang(zh-CN) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; }
.pdf:lang(zh-TW) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; }
.pdf:lang(ko-KR) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; }
.highlight-default {
	color: rgba(55, 53, 47, 1);
}
.highlight-gray {
	color: rgba(120, 119, 116, 1);
	fill: rgba(120, 119, 116, 1);
}
.highlight-brown {
	color: rgba(159, 107, 83, 1);
	fill: rgba(159, 107, 83, 1);
}
.highlight-orange {
	color: rgba(217, 115, 13, 1);
	fill: rgba(217, 115, 13, 1);
}
.highlight-yellow {
	color: rgba(203, 145, 47, 1);
	fill: rgba(203, 145, 47, 1);
}
.highlight-teal {
	color: rgba(68, 131, 97, 1);
	fill: rgba(68, 131, 97, 1);
}
.highlight-blue {
	color: rgba(51, 126, 169, 1);
	fill: rgba(51, 126, 169, 1);
}
.highlight-purple {
	color: rgba(144, 101, 176, 1);
	fill: rgba(144, 101, 176, 1);
}
.highlight-pink {
	color: rgba(193, 76, 138, 1);
	fill: rgba(193, 76, 138, 1);
}
.highlight-red {
	color: rgba(212, 76, 71, 1);
	fill: rgba(212, 76, 71, 1);
}
.highlight-default_background {
	color: rgba(55, 53, 47, 1);
}
.highlight-gray_background {
	background: rgba(241, 241, 239, 1);
}
.highlight-brown_background {
	background: rgba(244, 238, 238, 1);
}
.highlight-orange_background {
	background: rgba(251, 236, 221, 1);
}
.highlight-yellow_background {
	background: rgba(251, 237, 214, 1);
}
.highlight-teal_background {
	background: rgba(237, 243, 236, 1);
}
.highlight-blue_background {
	background: rgba(231, 243, 248, 1);
}
.highlight-purple_background {
	background: rgba(244, 240, 247, 0.8);
}
.highlight-pink_background {
	background: rgba(249, 238, 243, 0.8);
}
.highlight-red_background {
	background: rgba(253, 235, 236, 1);
}
.block-color-default {
	color: inherit;
	fill: inherit;
}
.block-color-gray {
	color: rgba(120, 119, 116, 1);
	fill: rgba(120, 119, 116, 1);
}
.block-color-brown {
	color: rgba(159, 107, 83, 1);
	fill: rgba(159, 107, 83, 1);
}
.block-color-orange {
	color: rgba(217, 115, 13, 1);
	fill: rgba(217, 115, 13, 1);
}
.block-color-yellow {
	color: rgba(203, 145, 47, 1);
	fill: rgba(203, 145, 47, 1);
}
.block-color-teal {
	color: rgba(68, 131, 97, 1);
	fill: rgba(68, 131, 97, 1);
}
.block-color-blue {
	color: rgba(51, 126, 169, 1);
	fill: rgba(51, 126, 169, 1);
}
.block-color-purple {
	color: rgba(144, 101, 176, 1);
	fill: rgba(144, 101, 176, 1);
}
.block-color-pink {
	color: rgba(193, 76, 138, 1);
	fill: rgba(193, 76, 138, 1);
}
.block-color-red {
	color: rgba(212, 76, 71, 1);
	fill: rgba(212, 76, 71, 1);
}
.block-color-default_background {
	color: inherit;
	fill: inherit;
}
.block-color-gray_background {
	background: rgba(241, 241, 239, 1);
}
.block-color-brown_background {
	background: rgba(244, 238, 238, 1);
}
.block-color-orange_background {
	background: rgba(251, 236, 221, 1);
}
.block-color-yellow_background {
	background: rgba(251, 237, 214, 1);
}
.block-color-teal_background {
	background: rgba(237, 243, 236, 1);
}
.block-color-blue_background {
	background: rgba(231, 243, 248, 1);
}
.block-color-purple_background {
	background: rgba(244, 240, 247, 0.8);
}
.block-color-pink_background {
	background: rgba(249, 238, 243, 0.8);
}
.block-color-red_background {
	background: rgba(253, 235, 236, 1);
}
.select-value-color-uiBlue { background-color: rgba(35, 131, 226, .07); }
.select-value-color-pink { background-color: rgba(245, 224, 233, 1); }
.select-value-color-purple { background-color: rgba(232, 222, 238, 1); }
.select-value-color-green { background-color: rgba(219, 237, 219, 1); }
.select-value-color-gray { background-color: rgba(227, 226, 224, 1); }
.select-value-color-transparentGray { background-color: rgba(227, 226, 224, 0); }
.select-value-color-translucentGray { background-color: rgba(0, 0, 0, 0.06); }
.select-value-color-orange { background-color: rgba(250, 222, 201, 1); }
.select-value-color-brown { background-color: rgba(238, 224, 218, 1); }
.select-value-color-red { background-color: rgba(255, 226, 221, 1); }
.select-value-color-yellow { background-color: rgba(249, 228, 188, 1); }
.select-value-color-blue { background-color: rgba(211, 229, 239, 1); }
.select-value-color-pageGlass { background-color: undefined; }
.select-value-color-washGlass { background-color: undefined; }

.checkbox {
	display: inline-flex;
	vertical-align: text-bottom;
	width: 16;
	height: 16;
	background-size: 16px;
	margin-left: 2px;
	margin-right: 5px;
}

.checkbox-on {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20width%3D%2216%22%20height%3D%2216%22%20fill%3D%22%2358A9D7%22%2F%3E%0A%3Cpath%20d%3D%22M6.71429%2012.2852L14%204.9995L12.7143%203.71436L6.71429%209.71378L3.28571%206.2831L2%207.57092L6.71429%2012.2852Z%22%20fill%3D%22white%22%2F%3E%0A%3C%2Fsvg%3E");
}

.checkbox-off {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20x%3D%220.75%22%20y%3D%220.75%22%20width%3D%2214.5%22%20height%3D%2214.5%22%20fill%3D%22white%22%20stroke%3D%22%2336352F%22%20stroke-width%3D%221.5%22%2F%3E%0A%3C%2Fsvg%3E");
}
	
</style></head><body><article id="b1425602-b386-4b12-9181-151c266944a9" class="page sans"><header><h1 class="page-title">서비스 이용약관</h1><p class="page-description"></p></header><div class="page-body"><p id="9ec5c11d-5510-44a4-9975-1345046e725c" class=""><strong>1. 목적</strong></p><p id="e4321312-26ab-4981-92f7-54a353c88ecf" class="">본 약관은 (주)효시컴퍼니 (이하 &quot;회사&quot;라 합니다)가 제공하는 교육 정보 서비스와 관련하여 (이하 “서비스”라 합니다) 회사와 이용자간에 서비스의 이용 조건 및 절차, 회사와 회원간의 권리, 의미 및 기타 필요한 사항을 규정함을 목적으로 합니다. 본 약관은 PC 통신, 스마트폰(안드로이드, 아이폰 등) 앱 등을 이용하는 전자상거래에 대해서도 그 성질에 반하지 않는 한 준용됩니다.</p><p id="2356bda4-952e-4a51-b1d9-49d16c0c5a73" class=""><strong>2. 용어의 정리</strong></p><p id="dfac8eb1-6807-415a-a220-60746acab3aa" class="">&quot;이용자&quot;라 함은 &quot;서비스&quot;에 접속하여 본 약관에 따라 &quot;회사&quot;가 제공하는 &quot;서비스&quot;를 이용하는 “회원&quot; 및 “비회원&quot;을 말합니다.</p><p id="5e07b136-6a1c-4d16-a06a-83b6861e1bbe" class="">&quot;회원&quot;이라 함은 “회사&quot;와 “회사”의 &quot;서비스&quot; 이용 계약을 체결하고 &quot;회원&quot; 아이디(ID)를 부여받은 &quot;이용자&quot;로서 “회사&quot;의 정보를 지속적으로 제공받으며 “회사&quot;가 제공하는 “서비스&quot;를 지속적으로 이용할 수 있는 자를 말합니다.</p><p id="c30aaf84-db06-4d15-b9b0-f0ee81dbaff3" class="">“유료 회원&quot;이라 함은 “회원&quot; 중 “회사&quot;가 제공하는 과금 “서비스”를 제공받기 위해서 일정 금액을 “회사&quot;에 납부한 “회원&quot;을 말합니다.</p><p id="11ee1114-8b99-45f6-a2e5-83b3e4fb40c1" class="">“서비스&quot;라 함은 접속 가능한 유,무선 단말기의 종류와는 상관없이 “회사&quot;가 제공하는 이용 가능한 모든 행위를 말하며, “회사&quot;가 제공하는 “콘텐츠”를 포함하는 개념이며, 본 계약에서는 “서비스 및 콘텐츠&quot;로 표시하는 경우도 있습니다.</p><p id="036bc257-77ea-485c-90a2-5f97ac693c53" class="">“콘텐츠&quot;라 함은 정보통신이용촉진 및 정보보호 등에 관한 법률 제 2조 1항 제 1호의 규정에 의한 정보통신망에서 사용되는 부호·문자·음성·음향 및 영상 등으로 표현된 자료 또는 정보로서, 그 보존 및 이용에 있어 효용을 높일 수 있도록 전자적 형태로 제작 또는 처리된 것을 말합니다.</p><p id="aba696c4-e7c8-46f0-a078-e56dca22467f" class="">&quot;개인정보&quot;라 함은 생존하는 개인에 관한 정보로서 해당 정보에 포함된 e-mail 주소, 전화번호, SNS 정보 등의 사항에 의하여 해당 개인을 식별할 수 있는 정보를 말합니다.</p><p id="6460a051-973a-48b0-ab98-916bffcbbfb1" class="">&quot;데이터&quot;이라 함은 &quot;회원&quot;이 서비스&quot;를 체험하는 모든 행위를 통해 만들어진 결과 (문제 풀이 결과, 질문 내용 등) 에 대한 정보를 의미합니다.</p><p id="31372849-54fa-44fc-9f44-7a06467a4545" class="">“탈퇴&quot;란 “회사&quot;또는 &quot;회원&quot;이 개통 후 이용 계약을 해약하는 것을 의미합니다.</p><p id="60edbcaf-11bf-4b96-8ad0-15fa938d955f" class="">이 약관에서 사용하는 용어 정의는 제 2조 [용어의 정리]에서 정하는 것을 제외하고는 관계법령 및 서비스 별 안내에서 정하는 바에 의합니다.</p><p id="7e02cca7-e0eb-4a7f-be2f-a0d9254e937f" class=""><strong>3. 약관의 효력과 변경</strong></p><p id="9dfc786d-a08c-40a8-8f7b-b945ac62654f" class="">본 약관은 &quot;회원&quot;이 약관의 내용에 동의하며 회원가입을 신청하고, &quot;회사&quot;가 그 신청에 대하여 승낙함으로써 효력이 발생합니다.</p><p id="8e4d8c0a-dc44-4522-b8ab-5bb227c1dbcc" class="">&quot;회사&quot;가 본 약관의 내용을 변경하는 경우 기존 &quot;회원&quot;들에게는 제 5조 [회원에 대한 통지]에서 명시한 방법으로 통지함으로써 효력이 발생합니다.</p><p id="6c5e9a0a-9c4f-47e6-b6da-8d3b91c11214" class="">“회사”는 합리적인 사유가 발생할 경우 &quot;약관의규제에관한법률&quot;, &quot;정보통신망이용촉진 및 정보보호등에관한법률&quot;(이하 &quot;정보통신망법&quot;)&quot; 등의 관련법령에 위배되지 않는 범위 안에서 약관을 개정할 수 있습니다.</p><p id="aacf6bf4-0687-4255-a047-edc3eb2b52db" class="">“회사”는 약관이 변경되는 경우에 변경된 약관의 내용과 시행일을 정하여, 그 시행일로부터 최소7일 (이용자에게 불리하거나 중대한 사항의 변경은 30일) 이전부터 시행일 후 상당한 기간 동안 공지하고, 기존 이용자에게는 변경된 약관, 적용일자 및 변경사유(변경될 내용 중 중요사항에 대한 설명을 포함)를 별도의 전자적 수단(카카오톡 메시지, 전자우편, 문자메시지, 서비스 내 전자쪽지발송, 홈페이지 초기화면에 게시, 알림 메시지를 띄우는 등의 방법)으로 통지합니다. 변경된 약관은 공지하거나 통지한 시행일로부터 효력이 발생합니다.</p><p id="1c8699fd-2d9c-4bf3-8ea8-009c1e204cdb" class="">“회사”가 제4항에 따라 변경된 약관을 공지 또는 통지하는 경우 “변경에 동의하지 아니한 경우 공지일 또는 통지를 받은 날로부터 7일(이용자에게 불리하거나 중대한 사항의 변경인 경우에는 30일) 내에 계약을 해지할 수 있으며, 계약해지의 의사표시를 하지 아니한 경우에는 변경에 동의한 것으로 본다.”라는 취지의 내용을 함께 통지합니다.</p><p id="aace9851-6726-47c9-9967-497886975003" class="">“회사”가 전항에 따라 변경된 약관을 공지 또는 통지하면서 회원에게 7일 기간 내에 의사표시를 하지 않으면 의사표시가 표명된 것으로 본다는 뜻을 명확하게 공지 또는 통지하였음에도 회원이 명시적으로 거부의 의사표시를 하지 아니한 경우 회원이 개정약관에 동의한 것으로 봅니다.</p><p id="85c2fb0c-b18c-42d9-84b2-24b933d8546a" class="">이 약관에 동의하는 것은 정기적으로 웹을 방문하여 약관의 변경사항을 확인하는 것에 동의함을 의미합니다. 변경된 약관에 대한 정보를 알지 못해 발생하는 이용자의 피해는 회사에서 책임지지 않습니다.</p><p id="8e76d20a-0965-428b-9ad5-009df4e72013" class="">회원이 변경된 약관에 동의하지 않을 경우 회사는 해당 회원의 탈퇴(해지)를 요청할 수 있습니다.</p><p id="133ad718-2fab-4930-aaf5-e63526721cd9" class=""><strong>4. 약관 외 준칙</strong></p><p id="bd8c34cc-5376-4dbf-a143-ccc1b5a86cf0" class="">이 약관에서 정하지 아니한 사항과 이 약관의 해석에 관하여는 온라인디지털콘텐츠산업발전법, 전자상거래 등에서의소비자보호에관한법률, 약관의규제에관한법률, 정보통신부장관이 정하는 디지털콘텐츠 이용자보호지침, 기타 관계법령 또는 상관례에 따릅니다.</p><p id="776997ef-cc13-40a2-997f-98c31ffcb204" class="">이 약관에서 정하지 아니한 사항에 대해서는 관계법령 또는 회사가 정한 서비스의 개별약관, 운영정책 및 규칙 등(이하 세부지침)의 규정에 따릅니다. 또한 본 약관과 세부지침이 충돌할 경우에는 세부지침에 따릅니다.</p><p id="4e674d2a-00bf-40cd-91be-c912874a8d40" class=""><strong>5. 회원에 대한 통지</strong></p><p id="49538ac0-8540-4b28-a497-3dea1c7ec270" class="">&quot;회사&quot;는 &quot;회원&quot;에게 알려야 할 상황이 발생하는 경우 전자적 수단(카카오톡 메시지, 전자우편, 문자메시지, 서비스 내 전자쪽지발송, 홈페이지 초기화면에 게시, 알림 메시지를 띄우는 등의 방법)으로 통지하거나, &quot;서비스&quot; 내에 공지 또는 팝업창을 게시하는 방법 등으로 통지할 수 있습니다.</p><p id="39324d59-b771-4c07-bd27-3f4fba66183d" class="">“회사”는 카카오톡 메시지 등을 통해 “회원”에게 만료 예정인 쿠폰, 상품, 이벤트 등을 안내 합니다. 만료 예정 알림은 서비스 상황에 따라 개인별로 알림 도착 시간이 상이할 수 있습니다.</p><p id="9eb9d4ce-c176-4a65-8a67-d1bbbb467b09" class="">전 항과 같이 통지한 경우 그때부터 7일 이내에 &quot;회원&quot;이 &quot;회사&quot;가 정하는 방법으로 그 통지 내용에 동의하지 않음을 표시하지 않을 경우 그 &quot;회원&quot;에게는 통지 내용이 도달하였고 통지 내용에 동의하였다고 간주합니다.</p><p id="d0609214-57a0-4f4e-a67c-b60d64b585e6" class="">통지 내용에 동의하지 아니하는 &quot;회원&quot;은 &quot;회사&quot;에 회원탈퇴를 요청할 수 있습니다.</p><p id="4d177eb9-24d1-4839-9b56-cd5897196fa6" class=""><strong>6. 회원가입 및 회원가입 신청</strong></p><p id="129c81ee-7745-4101-b145-ebc113143e31" class="">&quot;전 항과 같이 통지한 경우 그때부터 7일 이내에 &quot;회원&quot;이 &quot;회사&quot;가 정하는 방법으로 그 통지 내용에 동의하지 않음을 표시하지 않을 경우 그 &quot;회원&quot;에게는 통지 내용이 도달하였고 통지 내용에 동의하였다고 간주합니다.</p><p id="b94c0834-a785-4517-a5f3-0cb1472bc7a5" class="">전 항의 규정에 따라 회원가입을 할 때에는 “회사&quot;가 제공하는 “서비스&quot;의 원활한 이용을 위해 필요한 “개인정보”를 제공해야 합니다.</p><p id="edea1f31-9b5f-4618-976e-a570253754af" class=""><strong>7. 회원가입 신청에 대한 승낙</strong></p><p id="5d1ce4fd-b854-45ef-aa5d-e23b56644671" class="">승낙은 “회사&quot;가 “가입 신청자&quot;에게 “아이디&quot;를 부여함과 동시에 “서비스” 이용 개시를 통보함으로써 이루어 집니다.</p><p id="144f22a7-c85d-4538-8778-29dd37137761" class="">“회사&quot;는 다음 각 호에 해당하는 신청에 대하여는 승인을 하지 않거나 사후에 이용계약을 해지할 수 있습니다.</p><ul id="32d6469a-8523-49ae-8b11-fbf27d013e04" class="bulleted-list"><li style="list-style-type:disc">실명이 아니거나 타인의 명의를 이용한 경우</li></ul><ul id="05eef383-8966-4ba0-b6b5-cabade463b2a" class="bulleted-list"><li style="list-style-type:disc">등록내용에 허위의 정보를 기재하거나, 기재누락, 오기가 있는 경우</li></ul><ul id="4dedd97c-9aea-47a9-8cd0-9e8348e3e431" class="bulleted-list"><li style="list-style-type:disc">이미 가입된 회원과 전화번호나 전자우편주소가 동일한 경우</li></ul><ul id="95a85145-e273-4650-97d7-c9d84777ff72" class="bulleted-list"><li style="list-style-type:disc">부정한 용도 또는 영리를 추구할 목적으로 본 서비스를 이용하고자 하는 경우</li></ul><ul id="31fd5c1d-fad4-422c-a84d-cde0859314a6" class="bulleted-list"><li style="list-style-type:disc">기타 이 약관에 위배되거나 위법 또는 부당한 이용신청임이 확인된 경우 및 회사가 합리적인 판단에 의하여 필요하다고 인정하는 경우</li></ul><ul id="02cf8883-846f-464c-bd9d-5f84498d3026" class="bulleted-list"><li style="list-style-type:disc">“가입신청자”가 이 약관에 의하여 이전에 회원자격을 상실한 적이 있는 경우. 다만, 회원자격 상실 후 3년이 경과한 자로서 회사의 회원 재가입 승낙을 얻은 경우에는 예외로 함</li></ul><p id="6bc2cf76-75f3-489f-a070-fd6f09a88c7c" class="">“회사”는 “서비스” 이용신청이 다음 각 호에 해당하는 경우에는 그 신청에 대하여 승낙 제한사유가 해소될 때까지 승낙을 유보할 수 있습니다.</p><ul id="db8ed20a-4caf-4999-89a2-226ba49acbbc" class="bulleted-list"><li style="list-style-type:disc">“회사”가 설비의 여유가 없는 경우</li></ul><ul id="783ff65e-fce3-4d8b-8862-6d5fcb911661" class="bulleted-list"><li style="list-style-type:disc">“회사”의 기술상 지장이 있는 경우</li></ul><ul id="3ba648d7-97ab-413c-b16d-6ac7a013990d" class="bulleted-list"><li style="list-style-type:disc">“회사”는 “서비스” 이용신청을 한 자가 만 14세 미만 또는 피한정후견인인 경우에 법정대리인(부모등)의 동의 없는 이용신청에 대하여 승낙을 거절 또는 보류할 수 있습니다.</li></ul><p id="6d6daea0-f23f-40c5-9a9f-802535967ae0" class="">모든 &quot;회원&quot;은 반드시 이용자 본인의 e-mail 또는 회원가입에 필요한 정보를 제공하여야만 “서비스”를 이용할 수 있으며, 정확한 정보로 등록하지 않은 &quot;회원&quot;은 일체의 권리를 주장할 수 없습니다.</p><p id="bb9b8e51-fe72-48db-88d5-3d33b2c4b974" class="">회원가입은 &quot;회원&quot; 본인과 연락 가능한 정확한 정보로 가입해야 하며, “회사”는 관리 및 본인 확인 등을 위한 정보 확인 조치를 할 수 있습니다.</p><p id="06656a18-b7e6-43eb-ae7d-3c4742852af2" class="">타인의 정보를 도용하여 이용신청을 한 &quot;회원&quot;의 모든 ID는 삭제되며 관계 법령에 따라 처벌을 받을 수 있습니다</p><p id="fea83914-141c-4da9-858b-000ba1842d74" class=""><strong>8. 서비스 이용 범위 및 이용 시간</strong></p><p id="27edd0c3-a4db-46f7-a409-ff8380a46181" class="">“회사”는 “서비스” 제공과 관련한 “회사” 정책의 변경 등 기타 상당한 이유가 있는 경우 등 운영상, 기술상의 필요에 따라 제공하고 있는 “서비스”의 전부 또는 일부를 변경 또는 중단할 수 있습니다.</p><p id="50393be1-9faa-40ff-bfb3-d080ae571b52" class="">&quot;서비스&quot;는 &quot;회사&quot;의 업무상, 기술상 문제 등 기타 특별한 사정이 없는 한 매일 24시간 운영함을 원칙으로 합니다.</p><p id="3abe4d5b-4e53-4b5c-b19a-155987b3f773" class="">&quot;회사&quot;는 일부 &quot;서비스&quot;의 이용 가능 시간을 별도로 정할 수 있으며, 이 경우 사전에 “서비스” 제공화면에 공지합니다.</p><p id="93785a59-b8e3-471c-ab37-184cda4e5272" class="">“회사”는 “서비스”의 원활한 수행을 위하여 필요한 기간을 정하여 사전에 공지하고 “서비스”를 중지할 수 있습니다. 단, 불가피하게 긴급한 조치를 필요로 하는 경우 사후에 통지할 수 있습니다.</p><p id="c1f451b0-528d-4797-8ec3-a8cacbb5ae06" class="">“회사”는 무료로 제공되는 “서비스”의 일부 또는 전부를 회사의 정책 및 운영의 필요상 수정, 중단, 변경할 수 있으며, 이에 대하여 관련법에 특별한 규정이 없는 한 “회원”에게 별도의 보상을 하지 않습니다.</p><p id="6ce577a9-a151-4482-9997-63fd974be806" class=""><strong>9. 서비스 제공의 중지 및 제한</strong></p><p id="d8b58bdb-24ab-429f-a69a-ea2a2020d4ab" class="">“회사”는 컴퓨터 등 정보통신설비의 보수점검•교체 및 고장, 통신의 두절 등의 사유가 발생한 경우에는 “서비스”의 제공을 일시적으로 중단할 수 있습니다.</p><p id="de7e5958-9579-41e8-9131-a4bc9a7d34cb" class="">&quot;회사&quot;는 다음 각 호에 해당하는 경우 &quot;서비스&quot; 제공을 중지하거나 제한할 수 있습니다.</p><ul id="7b3c3c0e-aa35-49e5-b5fc-565e74601443" class="bulleted-list"><li style="list-style-type:disc">서비스용 설비의 최적화를 위한 시스템 점검 또는 설비 보수로 인해 부득이한 경우</li></ul><ul id="028640e6-d61b-4e42-877a-4d773a1735ce" class="bulleted-list"><li style="list-style-type:disc">분산서비스거부(DDoS) 공격 등에 의해 발생한 &quot;서비스&quot; 장애 복구를 위해 부득이한 경우</li></ul><ul id="cdfc225f-51c7-46cb-95c6-a1d6164a00a3" class="bulleted-list"><li style="list-style-type:disc">기타 서비스용 설비의 장애 또는 &quot;서비스&quot; 이용의 폭주 등으로 &quot;서비스&quot; 이용에 지장이 있는 경우</li></ul><ul id="a959e4e3-b93e-4038-8f78-9c8ab6f4a1bc" class="bulleted-list"><li style="list-style-type:disc">전기통신사업법에 규정된 기간통신사업자가 전기통신 서비스를 중지했을 경우</li></ul><ul id="d7c7a2f6-c707-4864-ae03-1d7ba683a91c" class="bulleted-list"><li style="list-style-type:disc">국가비상사태, 천재지변에 의해 부득이한 경우</li></ul><ul id="5818e8b2-ace1-4476-a941-76e155a8b239" class="bulleted-list"><li style="list-style-type:disc">기타 합리적인 이유가 있는 경우로서 &quot;회사&quot;가 필요하다고 인정하는 경우</li></ul><p id="eb83936b-d9bd-4f7b-b439-087b6354402f" class="">&quot;회사&quot;가 전 항들에 의하여 &quot;서비스&quot; 제공을 중지하거나 제한하는 경우 &quot;회사&quot;는 이를 사전 또는 사후에 &quot;회원&quot;에게 알려야 합니다. 다만, &quot;회사&quot;의 귀책사유 없이 &quot;회원&quot;에게 통지할 수 없는 경우에는 예외로 합니다.</p><p id="66626840-33f7-485d-ba76-964089fd715f" class="">“회사”와 계약한 출판사와의 계약 종료 및 변경 등의 사유로 서비스의 내용이 변경되거나, “서비스”가 중단될 수 있습니다.</p><p id="a80a9085-b79c-401d-bd14-1492c371bbd9" class="">전항의 사유로 “서비스”가 일시적으로 중단되는 경우 회사는 제5조에 정한 방법으로 이용자에게 통지합니다.</p><p id="8c1ca06b-0d8d-415c-979d-d033e84271fd" class="">회사의 귀책사유로 인하여 회원이 자유이용권(정액제) 서비스 이용기간 동안 “서비스”를 제공받을 수 없게 되는 경우, 회사는 회원이 그 기간만큼 이용할 수 있는 동일, 유사한 컨텐츠를 다시 제공합니다.</p><p id="a47f5fe8-919b-47a8-b877-4d080cb5fbc6" class="">사업종목의 전환, 사업의 포기, 업체간의 통합 등의 이유로 “서비스”를 제공할 수 없게 되는 경우에는 회사는 제5조에 정한 방법으로 이용자에게 통지하고 당초 회사에서 제시한 조건에 따라 소비자에게 보상합니다.</p><p id="7dc6a987-6c60-4bd3-b21b-bbb062ffa8f4" class=""><strong>10. 서비스의 내용</strong></p><p id="2cf7dc8c-6f4c-43e8-82b4-cf73b71e4681" class="">“회사”가 제공하는 서비스의 내용은 다음 각 호와 같습니다.</p><ul id="b04a64ca-2f93-433f-bbbc-ade1e46f9b42" class="bulleted-list"><li style="list-style-type:disc">회사는 AI 알고리즘을 이용하여 회원의 면접 점수 예측 및 취약부분에 대한 학습</li></ul><ul id="063a32d4-def9-459d-91b4-a6b8e638b920" class="bulleted-list"><li style="list-style-type:disc">교원 임용시험 관련 온라인 강의 제공</li></ul><ul id="380bd1c1-1093-45a0-8c1d-4298ef582a90" class="bulleted-list"><li style="list-style-type:disc">교원 임용시험 면접 문제 풀이 및 해설 제공</li></ul><ul id="161ada6f-33f0-48ed-b45f-12aaad235550" class="bulleted-list"><li style="list-style-type:disc">기타 교원 임용시험 학습과 관련된 제반 서비스 제공</li></ul><p id="2a1bed60-a446-4aba-a580-ac9987b6ae19" class="">“회사”는 필요한 경우 서비스의 내용을 추가 또는 변경할 수 있으며, 서비스의 내용의 추가, 변경으로 인하여 “회원”의 권리의무에 중대한 영향을 미치는 경우 “회사”는 추가 또는 변경된 서비스 내용을 그 적용일로부터 30일 전에 공지합니다.</p><p id="ba4ef871-fd2b-413a-895c-69c4168212ad" class="">“회사”가 제공하는 서비스 일부는 유선 또는 무선 네트워크가 연결된 상태에서 이용할 수 있으며, “회원”에게 유선 또는 무선 네트워크 사용에 대한 데이터 통화료가 부과될 수 있습니다. “회원”은 데이터 통화료를 부담할 의무가 있으며, “회사”는 이에 대하여 책임을 부담하지 않습니다.</p><p id="80c800b6-d08b-4036-bbf3-1631fb1a4e99" class=""><strong>11. 대금 결제</strong></p><p id="4c5b32d2-2504-4b14-90ab-8234c6963ff0" class="">“회원”은 다음 각 호의 방법으로 서비스 이용대금을 지급할 수 있습니다.</p><ul id="0b86a782-bf3a-4555-bb00-1ba5047d17ba" class="bulleted-list"><li style="list-style-type:disc">선불카드, 직불카드, 신용카드 등을 이용한 카드결제</li></ul><ul id="56c860c4-6f50-4e95-aafe-d32ad6106e41" class="bulleted-list"><li style="list-style-type:disc">폰뱅킹, 인터넷뱅킹 등을 활용한 실시간 계좌이체</li></ul><ul id="dd19494d-ca26-4b4f-853b-55159ad75e2a" class="bulleted-list"><li style="list-style-type:disc">구글스토어, 애플스토어 등을 이용한 인앱결제</li></ul><ul id="d0022c48-e856-4fc3-be29-bc34d31027ad" class="bulleted-list"><li style="list-style-type:disc">기타 회사가 제공하는 대금 지급 방법을 활용한 결제</li></ul><p id="6e36b1eb-c149-4d33-a9f8-d8409a7d961f" class="">“회원”은 서비스 이용대금 결제시 본인이 입력한 정보를 확인하여야 하며, 정보 오입력 등으로 인하여 발생하는 일체의 책임을 부담합니다.</p><p id="17f42ad1-2172-4043-90d9-66efc8ee63c6" class="">“회사”는 “회원”이 사용한 결제수단에 대하여 정당한 사용 권한을 가지고 있는지 확인할 수 있으며, 확인이 완료될 때까지 거래 진행을 중지하거나 확인이 불가능한 경우 해당거래를 취소할 수 있습니다.</p><p id="a9dbe13f-c7f3-47bb-8da7-8779525d0e73" class=""><strong>12. 회원의 청약철회 등</strong></p><p id="6efb8044-7c78-4cc1-b3fb-276dd2e0f62f" class="">“회원”은 서비스 이용 개시일로부터 7일 이내(이하 “청약철회 기간”)에 서비스 이용계약에 대한 청약철회를 할 수 있습니다.</p><p id="7f0ce75d-a13a-4934-8082-3368de922155" class="">제1항에도 불구하고, 회원은 다음 각 호의 어느 하나에 해당하는 경우에는 청약철회를 할 수 없습니다.</p><ul id="9a07e778-e59a-42e5-b449-00869f8903d0" class="bulleted-list"><li style="list-style-type:disc">“회원”에게 책임 있는 사유로 재화 등이 멸실 또는 훼손된 경우(다만, 재화 등의 내용을 확인하기 위하여 포장 등을 훼손한 경우에는 제외됩니다.)</li></ul><ul id="98fb92b9-f665-4656-8984-035f8df7945d" class="bulleted-list"><li style="list-style-type:disc">“회원”의 사용 또는 일부 소비로 재화등의 가치가 현저히 감소한 경우</li></ul><ul id="3f367e1c-75dc-43e3-b765-7ac36ab545b7" class="bulleted-list"><li style="list-style-type:disc">시간이 지나 다시 판매하기 곤란할 정도로 재화등의 가치가 현저히 감소한 경우</li></ul><ul id="d87c6d76-7960-4bb6-aee7-7d062cb8b5cc" class="bulleted-list"><li style="list-style-type:disc">복제가 가능한 재화등의 포장을 훼손한 경우</li></ul><ul id="155ddfb5-5e0c-499b-a9d1-b99c905b8108" class="bulleted-list"><li style="list-style-type:disc">용역 또는 문화산업진흥 기본법 제2조 제5호의 디지털콘텐츠 제공이 개시된 경우</li></ul><p id="3459c2a5-08e6-46bf-882e-f8ca47e5d4bb" class="">“회사”는 제2항 b호 내지 e호에 해당하는 재화 또는 서비스를 공급하는 경우, 전자상거래 등에서의 소비자보호에 관한 법률 제17조 제6항에 따라 회원의 청약철회 등의 권리행사가 방해받지 않도록 필요한 조치를 취하여야 합니다.</p><p id="dfb78b33-f601-4304-87e8-15013c1b1250" class="">“회원”은 제1항에도 불구하고, 서비스의 내용이 표시, 광고의 내용과 다르거나 계약내용과 다르게 이행된 경우에는 해당 서비스를 공급받은 날로부터 3개월 이내, 그 사실을 안 날 또는 알 수 있었던 날로부터 30일 이내에 청약철회를 할 수 있습니다.</p><p id="a7e4ad49-db67-4d66-bf9f-4894684cb631" class="">“회원”은 청약철회 기간이 도과한 후에도 서비스 이용계약을 해지할 수 있습니다.</p><p id="56e9134f-7fba-4200-83bc-669c51c0a5da" class=""><strong>13. 청약철회 또는 계약해지의 효과</strong></p><p id="8fa624c5-0bc0-49f3-b565-299142a99ee6" class="">&quot;회사&quot;는 &quot;회원&quot;으로부터 청약철회 또는 계약해지의 의사표시를 수령한 날로부터 3영업일 이내에 대금의 결제와 동일한 방법으로 이를 환불하여야 하며, 동일한 방법으로 환불이 불가능할 때에는 이를 사전에 고지하여야 합니다. 다만, (i) 회사가 재화를 공급한 경우에는 재화를 반환받은 날, (ii) 수납확인이 필요한 결제수단의 경우에는 수납확인일로부터 3영업일 이내에 이를 환불하도록 합니다.</p><p id="5a60b10b-068d-4211-ace5-ce4921699d16" class=""><strong>14. 대금의 환불조치</strong></p><p id="fc9167fe-b522-4963-a276-0eab385d8aba" class="">“회사&quot;는 “회원”으로부터 청약철회 또는 해지의 의사표시를 받거나, “회사”의 사정으로 인하여 서비스 이용계약을 종료하는 경우 다음과 같이 “회원”에게 서비스 이용대금의 전부 또는 일부를 반환합니다.</p><table id="be03ba0e-a0a5-4ff2-b6f0-fe2177fb7d86" class="simple-table"><tbody><tr id="7b98cb62-3d82-49c7-9633-280d44886508"><td id="IaM=" class=""><strong>구분</strong></td><td id="Vivo" class=""><strong>반환 금액</strong></td></tr><tr id="bbd60915-48f2-4ba6-8b47-5f1482134a00"><td id="IaM=" class="">회원이 서비스를 이용하지 않고, 서비스 이용 개시일로부터 7일 이내에 청약철회를 한 경우</td><td id="Vivo" class="">서비스 이용대금 전액 반환</td></tr><tr id="4ef7ffde-a08f-4ecd-a71d-d923e64644c2"><td id="IaM=" class="">총 수강기간이 1개월 이내이며, 총 수강기간의 1/3이 경과하기 전</td><td id="Vivo" class="">서비스 이용대금 2/3에 해당하는 금액 반환</td></tr><tr id="394b6bb9-5a67-4564-a9d6-9fe72a02664e"><td id="IaM=" class="">총 수강기간이 1개월 이내이며, 총 수강기간의 1/2이 경과하기 전</td><td id="Vivo" class="">서비스 이용대금 1/2에 해당하는 금액 반환</td></tr><tr id="3f38d197-9f97-4d8a-bcce-c39ca9eb442f"><td id="IaM=" class="">총 수강기간이 1개월 이내이며, 총 수강기간의 1/2이 경과한 경우</td><td id="Vivo" class="">서비스 이용대금 반환 불가</td></tr><tr id="c28c9771-0f3f-4ae3-94c2-b6f61274b5b4"><td id="IaM=" class="">총 수강기간이 1개월을 초과하는 경우</td><td id="Vivo" class="">서비스 이용대금- [1일 서비스 이용요금 X 기 이용일수]를 공제하고 남은 금액</td></tr><tr id="1bc07939-31a6-4c5f-bd70-e9dee8fd776e"><td id="IaM=" class="">비고</td><td id="Vivo" class="">회원이 정상가격이 아닌 할인가격으로 서비스 이용대금을 결제한 경우, 정상가격을 기준으로 1일 서비스 이용요금을 산정하여 기 이용일수만큼 공제함</td></tr></tbody></table><p id="70896c95-0788-443b-8b74-af650e49760a" class="">“회원”이 일회성 이벤트, 프로모션 등을 통하여 서비스 이용계약을 체결하는 경우, “회사”는 이에 대하여 별도의 청약철회, 환불 정책을 수립할 수 있으며, “회원”이 해당 서비스 이용계약을 체결하는 경우, 청약철회 및 환불정책을 고지합니다. 명확히 하자면, 별도의 청약철회, 환불 정책이 있는 경우 본 이용약관에 우선하여 적용됩니다.</p><ul id="62e06c95-351f-4915-b004-ade25de0a122" class="bulleted-list"><li style="list-style-type:disc">“회사”가 “회원”에게 서비스 제공 이외에 재화를 공급하는 경우(이하 “패키지 상품”) “회사”는 아래와 같이 환불조치를 취합니다.</li></ul><ul id="0cd4d631-d61d-459b-81a0-a253bbf00e5d" class="bulleted-list"><li style="list-style-type:disc">“회원”은 재화를 배송받은 날로부터 7일 이내에 재화를 반환할 수 있고, “회사”는 패키지 상품에 대한 이용대금을 환불합니다.</li></ul><p id="4a70d7b5-e242-41bd-825b-f557ebf510f0" class="">단, (i) “회원”에게 책임 있는 사유로 재화가 멸실 또는 훼손되거나 (ii) “회원”의 사용 또는 일부 소비로 재화의 가치가 현저히 감소한 경우 재화는 반품처리되지 않습니다. 재화 반품에 소요되는 비용은 “회원”이 부담합니다.</p><p id="65debda7-f934-4043-a135-720cffdef1f6" class=""><strong>15. 과오금 등</strong></p><p id="5de440ed-15c5-4bb9-8252-902dd25304f2" class="">“회사”는 과오금이 발생할 경우 이용대금의 결제와 동일한 방법으로 과오금 전액을 환불하여야 합니다. 다만, 동일한 방법으로 환불이 불가능할 때는 이를 사전에 고지합니다.</p><p id="f9c5e489-98ee-4be1-a9d4-e51a270cdf4e" class="">“회사&quot;의 책임 있는 사유로 과오금이 발생한 경우 “회사&quot;는 계약비용, 수수료 등에 관계없이 과오금 전액을 환불합니다. 다만, “회원&quot;의 책임 있는 사유로 과오금이 발생한 경우, “회사&quot;가 과오금을 환불하는 데 소요되는 비용은 합리적인 범위 내에서 “회원&quot;이 부담하여야 합니다.</p><p id="e2441990-9c37-4e39-9530-a7c4c3c67016" class="">“회사&quot;는 “서비스&quot; 사용료를 과소납입한 “회원”에게 해당 금액에 해당하는 부분을 추가로 청구할 수 있으며, 청구에 대해 불응시 “서비스” 중지 및 제공기간이 축소될 수 있습니다.</p><p id="c761e49b-232d-44a1-b7e3-234dbe3a8e09" class=""><strong>16. 회사의 의무</strong></p><p id="97d91881-eb30-4094-b5ad-fa7e5bef3ce3" class="">&quot;회사&quot;는 지속적, 안정적으로 &quot;서비스&quot;를 제공하기 위해 최선을 다합니다.</p><p id="ef6957b0-aefd-43ed-b098-4d06abb9f845" class="">“회사”는 &quot;회원&quot;이 안전하게 “서비스”를 이용할 수 있도록 개인정보(신용정보 포함)보호를 위해 개인정보취급방침을 수립하여 공시하고 준수합니다.</p><p id="be4f39b4-4dab-4cb2-96f9-0e71cb9a4b3c" class="">&quot;회사&quot;는 &quot;회원&quot;의 &quot;개인정보&quot;를 그 &quot;회원&quot;의 동의 없이 제3자에게 누설, 배포하지 않는 것을 원칙으로 합니다. 단, 다음 각 호의 1에 해당하는 경우에는 예외로 합니다.</p><ul id="50e8f09e-e122-4274-8c9d-e3e256401a52" class="bulleted-list"><li style="list-style-type:disc">전기통신기본법 등 법률의 규정에 의한 국가기관의 요구가 있는 경우</li></ul><ul id="3a2043e9-e770-46d3-b76b-fb89f3ac86c4" class="bulleted-list"><li style="list-style-type:disc">범죄에 대한 수사상의 목적이 있거나 정보통신윤리위원회의 요청이 있는 경우</li></ul><ul id="5f40c606-c431-4f89-ab50-c9e14cb829d6" class="bulleted-list"><li style="list-style-type:disc">기타 관계 법령이 정한 절차에 따른 요청이 있는 경우</li></ul><p id="ff382f1d-5fd0-4945-bf13-36c81b0d7708" class="">회사는 서비스이용과 관련하여 회원으로부터 제기된 의견이나 불만이 정당하다고 인정할 경우에는 이를 처리하여야 합니다. 회원이 제기한 의견이나 불만사항에 대해서는 연락 가능한 수단을 통하여 회원에게 처리과정 및 결과를 전달합니다.</p><p id="b9696bb1-2a21-444e-9e65-7d5daf6bedb5" class=""><strong>17. 개별 서비스에 대한 약관 및 이용조건</strong></p><p id="9d6509e6-4496-4e21-9f12-8b128367ca35" class="">“회사”는 개별 서비스와 관련한 별도의 약관 및 이용정책을 둘 수 있으며, 개별 서비스에서 별도로 적용되는 약관에 대한 동의는 &quot;회원&quot;이 개별서비스를 최초로 이용할 경우 별도의 동의절차를 거치게 됩니다. 이 경우 개별 서비스에 대한 이용약관 등이 본 약관에 우선합니다.</p><p id="ec157ce3-7320-4873-88c7-076f50716589" class="">전항에도 불구하고 “회사”는 개별 서비스에 대한 이용정책에 대해서는 “서비스”를 통해 공지할 수 있으며, &quot;회원&quot;은 이용정책을 숙지하고 준수하여야 합니다.</p><p id="b93fa9fc-94de-46e9-88ed-c4f4c5a79471" class=""><strong>18. 개인정보 보호 등</strong></p><p id="5a101c3e-de8b-4ac2-9784-18daa91548e4" class="">&quot;회사&quot;는 &quot;회원&quot;의 &quot;개인정보&quot; 수집 시 필요한 최소한의 정보를 수집합니다.</p><p id="a951c845-a72b-48ee-be9a-fba5e3a97d9c" class="">&quot;회사&quot;는 &quot;회원&quot;의 &quot;개인정보&quot;를 수집 시 각 호의 1에 해당하는 경우를 제외하고는 그 &quot;회원&quot;의 동의를 받습니다.</p><ul id="580aa212-c78c-49d6-9337-3398fbd6d22d" class="bulleted-list"><li style="list-style-type:disc">법률에 특별한 규정이 있는 경우</li></ul><ul id="2dec81ab-78b1-49d5-9765-40738ca14762" class="bulleted-list"><li style="list-style-type:disc">전자거래 계약의 이행을 위하여 필요한 경우</li></ul><ul id="0c4fc108-1dbf-455d-aa5a-e8c87db74b11" class="bulleted-list"><li style="list-style-type:disc">&quot;서비스&quot; 제공에 따른 요금 정산을 위하여 필요한 경우</li></ul><p id="0744682b-5ee9-4b9c-9908-da17c45987ee" class="">&quot;회사&quot;는 &quot;회원&quot;의 &quot;개인정보&quot;를 그 &quot;회원&quot;의 동의 없이 목적 외로 사용하거나 제3자에게 제공할 수 없습니다. 단, 다음 각 호의 1에 해당하는 경우에는 예외로 합니다.</p><ul id="961be4cf-7d7c-40d0-a07e-3e73e8d62236" class="bulleted-list"><li style="list-style-type:disc">약관 또는 법률에 특별한 규정이 있는 경우</li></ul><ul id="eeff9f6b-a756-4ba7-aff8-541a53d1f68f" class="bulleted-list"><li style="list-style-type:disc">&quot;서비스&quot; 제공에 따른 요금 정산을 위해 필요한 경우</li></ul><ul id="f7c8abef-3ca1-43d9-980d-9df3d2ed0143" class="bulleted-list"><li style="list-style-type:disc">통계작성, 학술연구 또는 시장조사를 위하여 필요한 경우로서 특정 개인을 식별할 수 없는 형태로 제공되는 경우</li></ul><ul id="d057176c-1443-4588-8b3f-c28e243e6e24" class="bulleted-list"><li style="list-style-type:disc">&quot;회사&quot;와 관련하여 합병, 인수, 포괄적 영업양도 등이 있는 경우 합병 후 회사, 인수회사, 영업양수인에 대하여 제공하는 경우</li></ul><p id="c487e069-f7d1-4d78-b765-ee41c8575013" class="">&quot;회원&quot;은 &quot;서비스&quot;상의 개인정보관리 시스템을 통해 언제든지 본인의 개인정보를 열람하고 수정할 수 있습니다. 다만, &quot;아이디&quot;는 변경할 수 없습니다.</p><p id="e2e3e11a-aed0-4447-9ea6-236016232bc7" class="">&quot;회원&quot;은 가입신청 시 기재한 사항이 변경되었을 경우 온라인으로 수정해야 하며, 이를 수정하지 아니하여 발생하는 문제의 책임은 &quot;회원&quot;에게 있습니다.</p><p id="2078d2b9-d965-49b6-9249-0236f5c73a57" class="">&quot;개인정보&quot;의 수집목적 또는 제공받은 목적을 달성한 때에는 당해 &quot;개인정보&quot;를 폐기합니다.</p><p id="707c1a8a-a300-43cc-8df8-9677b770864b" class="">전 항의 경우라도 &quot;회사&quot;가 사전에 개인정보취급방침에 규정하여 &quot;회원&quot;의 동의를 받거나 관련 법령에 따라 일정기간 &quot;개인정보&quot;를 보관해야 하는 경우 &quot;회사&quot;는 예외적으로 일정기간 &quot;개인정보&quot;를 보관할 수 있습니다.</p><p id="bd2ea7e3-a56f-4eb3-86db-ba1b106ff1e1" class="">&quot;회사&quot;는 수집된 개인정보의 취급 및 관리의 업무를 스스로 수행함을 원칙으로 하나, 필요한 경우 업무의 일부 또는 전부를 위탁업체에 위탁할 수 있으며 위탁업체의 세부내용은 &quot;회사&quot; 홈페이지의 &quot;개인정보취급방침&quot;을 통해 확인할 수 있습니다.</p><p id="c3158c5b-f5d1-4f48-8460-72de3bd3a6cf" class="">“회사”는 최종 사용일로부터 연속하여 1년 동안 서비스 사용 이력이 없는 경우 &quot;정보통신망 이용촉진 및 정보보호에 관한 법률&quot;의 규정에 의하여 이용자정보를 영구적으로 삭제할 수 있습니다. 단, 유료결제 상품을 보유 하고 있을 경우 삭제 대상에서 제외 되며 관련 법령의 규정에 의하여 보존할 필요가 있는 경우 회사는 관계법령에서 정한 일정기간 동안 이용자정보를 보관합니다</p><p id="36c376b7-2c62-43dc-9516-eff442f43526" class=""><strong>19. 이용자의 아이디와 비밀번호 관리에 대한 의무</strong></p><p id="e7c660ca-fda9-45fe-9053-03d9114a43e6" class="">&quot;아이디&quot;와 ”비밀번호”에 관한 모든 관리책임은 &quot;회원&quot;에게 있습니다.</p><p id="2f50e7fe-3cad-4576-bda3-19411e4793b1" class="">&quot;회원&quot;의 &quot;아이디&quot; 및 “비밀번호”의 관리에 관하여 &quot;회사&quot;의 고의 및 중과실이 없는 한, &quot;회원&quot;에게 부여된 &quot;아이디&quot;와 “비밀번호”의 관리소홀, 부정사용에 의하여 발생하는 모든 결과에 대한 책임은 &quot;회원&quot;에게 있습니다.</p><p id="e722f4fb-92c1-4c6f-ade5-8c7772600723" class="">자신의 &quot;아이디&quot;가 부정하게 사용된 경우, &quot;회원&quot;은 반드시 &quot;회사&quot;에 그 사실을 통보해야 합니다.</p><p id="9e76966a-9753-45af-a01f-e4dedd0c05a6" class="">&quot;회원&quot;이 제20조 [이용자의 의무]에 따른 통지를 하지 않거나 “회사”의 조치에 응하지 아니하여 발생하는 모든 불이익에 대한 책임은 “회원”에게 있습니다.</p><p id="c80b1bd9-5a40-4815-9c0f-bd811ad6d826" class=""><strong>20. 이용자의 의무</strong></p><p id="aea2c533-a485-429a-9044-bf30d433a1d2" class="">&quot;회원&quot;은 &quot;서비스&quot;를 이용할 때 다음 각 호의 행위를 해서는 안 됩니다.</p><ul id="11319b23-c0a6-446e-83d7-7b2e26396547" class="bulleted-list"><li style="list-style-type:disc">다른 &quot;회원&quot;의 &quot;아이디&quot;를 부정하게 사용하는 행위</li></ul><ul id="ac98abcb-cdf9-4faf-91bc-7b890b82e750" class="bulleted-list"><li style="list-style-type:disc">자신의 &quot;아이디&quot; 및 &quot;서비스&quot;를 타인이 사용하도록 하는 행위</li></ul><ul id="33880782-9eb2-4d3f-bc69-75b96890d79a" class="bulleted-list"><li style="list-style-type:disc">다량의 정보를 전송하여 “서비스”의 안정적인 운영을 방해하는 행위</li></ul><ul id="06ce96d8-6a66-446a-bc9a-c821df61bbd8" class="bulleted-list"><li style="list-style-type:disc">“서비스&quot;에서 얻은 정보를 &quot;회사&quot;의 사전 승낙 없이 &quot;회원&quot;의 정당한 이용 이외의 목적으로 복제하거나 이를 출판 및 방송 등에 사용하거나 제 3자에게 제공하는 행위</li></ul><ul id="5bae078b-fd90-434d-a684-640500aca621" class="bulleted-list"><li style="list-style-type:disc">&quot;회사&quot; 또는 제3자의 저작권 등 지적 재산권 기타 권리를 침해하거나 침해하려는 행위</li></ul><ul id="fc28516e-c17f-4777-9e3e-3ce7a60acf7d" class="bulleted-list"><li style="list-style-type:disc">공공질서 및 미풍양속에 위반되는 내용의 정보, 문장, 도형 등을 타인에게 유포하는 행위</li></ul><ul id="da5ccb03-e9c8-4912-8919-f7f2e6e5bdaa" class="bulleted-list"><li style="list-style-type:disc">범죄와 결부된다고 객관적으로 판단되는 행위</li></ul><ul id="4c4ba911-d7cf-4958-8425-4c387061cfc7" class="bulleted-list"><li style="list-style-type:disc">외설 또는 폭력적인 메시지, 화상, 음성 기타 공공질서 미풍양속에 반하는 정보를 “서비스”에 공개 또는 게시하는 행위</li></ul><ul id="ba347191-4ab8-40a8-b039-c073cf056513" class="bulleted-list"><li style="list-style-type:disc">고객센터 상담 내용이 욕설, 폭언, 성희롱 등에 해당하는 행위</li></ul><ul id="cdf29797-745f-4db3-96ee-d914cf888845" class="bulleted-list"><li style="list-style-type:disc">“회사”의 운영정책 및 기타 관계 법령에 위배되는 행위</li></ul><ul id="fab12a8c-9706-4987-98c3-a4529e194f03" class="bulleted-list"><li style="list-style-type:disc">“수강료”를 부정하게 사용하는 등의 행위</li></ul><ul id="60188d48-2036-4352-8653-a292f78a393f" class="bulleted-list"><li style="list-style-type:disc">리버스엔지니어링, 디컴파일, 디스어셈블 및 기타 일체의 가공행위를 통하여 서비스를 복제, 분해 또 모방 기타 변형하는 행위</li></ul><ul id="c54a9e88-e637-4a2e-bed7-b23c469cd82c" class="bulleted-list"><li style="list-style-type:disc">자동 접속 프로그램 등을 사용하는 등 정상적인 사용 법과 다른 방법으로 서비스를 이용하여 회사의 서버에 부하를 일으켜 회사의 정상적인 서비스를 방해하는 행위</li></ul><p id="4140036c-4f38-49da-9ac0-7fca7d81c69f" class="">&quot;회원&quot;은 본 약관에 규정하는 사항과 서비스 이용안내 또는 주의사항을 준수해야 합니다.</p><p id="e86fa20d-3aa8-4e2a-bf4e-e3440d9e4c43" class="">&quot;회원&quot;은 사항 별로 &quot;회사&quot;가 서비스 공지사항에 게시하거나 별도로 공지한 사항을 준수해야 합니다.</p><p id="d7727e8d-a2f3-4f7e-aeb4-849787f79960" class="">&quot;회원&quot;은 &quot;회사&quot;의 명시적인 동의가 없는 한 &quot;서비스&quot;의 이용권한 기타 이용 계약상의 지위를 타인에게 양도, 증여할 수 없으며, 이를 담보로 제공할 수 없습니다.</p><p id="4a4f4136-8e1f-4634-9f4d-5ab6df2f3075" class="">“회원”은 “회사”에서 제공하는 서비스를 본래의 이용목적 이외의 용도로 사용해서는 안됩니다. 이를 위반할 경우에는 본 약관 및 각 서비스 운영정책에 따라 “회원”의 서비스 이용을 제한하거나 아이디의 삭제, 수사기관의 고발 조치 등 적법한 조치를 포함한 제재를 가할 수 있습니다.</p><p id="4b5af779-52cc-4c96-8f26-59890cac413f" class="">&quot;회사&quot;는 &quot;회원&quot;이 제 20조 [이용자의 의무] 에 명시된 내용을 위반하였을 경우 사전 통지 없이 계약을 해지하거나 &quot;서비스&quot; 이용을 제한할 수 있습니다.</p><p id="e5e6fde3-dee9-44c4-aab5-52e17a357a76" class="">&quot;회사&quot;가 전 항에 따라 계약을 해지하거나 &quot;서비스&quot; 이용을 제한하는 경우 이를 &quot;회원&quot;에게 알립니다. 다만, &quot;회사&quot;의 귀책사유 없이 &quot;회원&quot;에게 알릴 수 없는 경우에는 예외로 합니다.</p><p id="8d59ef55-4404-4407-9c1e-2c4b4466b84b" class=""><strong>21. 이용계약의 종료</strong></p><p id="5ecef201-2f5a-431e-8c25-60ae666735c8" class="">&quot;회원&quot;이 &quot;서비스&quot;의 중단을 요구하는 경우에는 &quot;회원&quot; 본인 또는 &quot;회원&quot;의 법정대리인이 &quot;회사&quot;가 요구하는 절차에 따라 회원 탈퇴 신청을 하여야 합니다.</p><p id="f51f06f1-4da8-4245-b6b4-fbfb1ac455fa" class="">&quot;회원&quot;의 회원 탈퇴 신청을 확인한 경우 &quot;회사&quot;는 신속히 회원 탈퇴 절차를 처리하며, 관련법 및 개인정보취급방침에 따라 &quot;회사&quot;가 회원정보를 보유하는 경우를 제외하고는 탈퇴 완료 후 지체 없이 &quot;회원&quot;의 개인정보를 파기합니다.</p><p id="627eff21-9855-4f4b-8ec0-1d25bbf47053" class="">&quot;회원&quot;이 “서비스&quot; 중단을 요청하는 경우, &quot;회원&quot;이 “서비스&quot;를 사용하면서 만들어 낸 누적 “데이터&quot;는 파기 되지 않습니다.</p><p id="e563e432-c8ae-4827-bc77-c38751ff6e4b" class=""><strong>22. 회원 자격 상실 및 정지</strong></p><p id="ee25bc86-7b5d-4b20-b592-0c74e6c983eb" class="">&quot;회사&quot;는 &quot;회원&quot;이 제 20조 [이용자의 의무]에 위반하는 행위를 하였을 경우, 사전 통지 없이 경고, 일시정지, 영구이용 정지 등을 통해 회원 자격을 상실 또는 정지시킬 수 있습니다.</p><p id="a8e3e288-15a0-4021-8b80-64eacfdb8534" class="">&quot;회사&quot;가 전 항에 따라 회원 자격을 상실시키거나 제한하는 경우에는 &quot;회사&quot;는 이를 &quot;회원&quot;에게 알립니다. 다만, &quot;회사&quot;의 귀책사유 없이 &quot;회원&quot;에게 알릴 수 없는 경우에는 예외로 합니다.</p><p id="5c2b470f-8a65-4590-a157-c6a9252bacd2" class="">&quot;회사&quot;가 제1항에 따라 &quot;회원&quot; 자격을 상실시키거나 제한하는 경우 해당 &quot;회원&quot;에 대하여는 &quot;회사&quot;가 제공하는 모든 &quot;서비스&quot;의 이용을 중단시킬 수 있고, 해당 &quot;회원&quot;은 &quot;회사&quot;에 대하여 중단 이후의 &quot;서비스&quot;에 대한 환불을 요구할 수 없습니다.</p><p id="0087ac39-6e72-457c-b5e3-a18ba706200c" class="">“회사”는 &quot;회원&quot;이 계속해서 1년 이상 로그인하지 않는 경우, 회원정보의 보호 및 운영의 효율성을 위해 이용을 제한할 수 있습니다.</p><p id="7d71813d-608f-4c85-985e-d8731798e32b" class="">본 조에 따라 서비스 이용을 제한하거나 계약을 해지하는 경우에는 회사는 제 5조 [회원에 대한 통지]에 명시된 방침에 따라 통지합니다.</p><p id="16e26316-1437-4cfc-962f-79223fe877ab" class="">“회원”은 본 조 및 제20조 제6항 등에 따른 이용제한 등에 대해 “회사”가 정한 절차에 따라 이의신청을 할 수 있습니다. 이 때 이의가 정당하다고 회사가 인정하는 경우 “회사”는 즉시 서비스의 이용을 재개합니다.</p><p id="dae7ce5c-4d7f-4ab1-8809-c6fc3f6f6440" class="">본 조에 따라 이용제한이 되는 경우 서비스 이용을 통해 획득한 혜택 등도 모두 이용 중단, 또는 소멸되며, “회사”는 이에 대해 별도로 보상하지 않습니다.</p><p id="beeccee1-78d5-4c32-ad1f-aefcb8c8f0e4" class=""><strong>23. 저작권</strong></p><p id="2f1242bd-ee60-4cff-a6ab-eace2bc76af4" class="">&quot;회사&quot;가 자체 제작한 “콘텐츠”와 &quot;회사&quot;가 제3자로부터 저작권을 양수받은 “콘텐츠”에 대한 저작권은 &quot;회사&quot;에 있습니다.</p><p id="6f906e17-a34c-407d-9263-5ced3cd6d754" class="">&quot;회사&quot;가 제3자로부터 이용 허락을 받은 “콘텐츠”에 대한 저작권은 제3자에게 있고 &quot;회사&quot;는 그에 대한 사용권을 가집니다.</p><p id="e57d02b1-fd36-48ee-97e6-32e91246f1c0" class="">&quot;회원&quot;은 &quot;회사&quot;가 제공하는 &quot;서비스&quot;를 이용함으로써 얻은 정보를 &quot;회사&quot;의 사전 승낙 없이 복제, 송신, 출판, 배포, 방송 기타 방법에 의하여 영리, 비영리의 목적으로 이용하거나 제3자에게 이용하게 할 수 없습니다.</p><p id="a6796686-7544-4579-b56c-69bd48dec886" class="">&quot;회사&quot;는 &quot;회사&quot; 또는 제3자의 저작권을 보호하기 위하여 &quot;회원&quot;이 &quot;서비스&quot;를 이용하는 동안 &quot;회원&quot;의 유,무선 기기 상 소프트웨어가 실행되는 것을 감지하여 자동으로 차단하는 프로그램을 사용할 수 있습니다.</p><p id="2d5f677e-905d-4448-954c-c05ecd404709" class=""><strong>24. 손해배상</strong></p><p id="4aa0cc71-de3e-4d5a-9a4e-7288d425c3f6" class="">“회사” 또는 “회원”은 상대방의 귀책에 따라 손해가 발생하는 경우 손해배상을 청구할 수 있습니다. 다만, &quot;회사&quot;는 무료서비스의 장애, 제공 중단, 보관된 자료 멸실 또는 삭제, 변조 등으로 인한 손해에 대하여는 배상 하지 않습니다.</p><p id="36be14ec-9d91-4192-ad4b-756aff7e5316" class="">&quot;회원&quot;이 본 약관의 규정을 위반하여 &quot;회사&quot; 또는 제3자에게 손해가 발생하게 되는 경우, 약관을 위반한 &quot;회원&quot;은 &quot;회사&quot; 및 제3자에게 발생한 손해를 배상할 책임이 있습니다</p><p id="3fbf3e06-f69c-4397-ab4c-6a62a77c8936" class=""><strong>25. 면책조항</strong></p><p id="776aaa83-82b6-4c24-9671-305b2943328f" class="">&quot;회사&quot;는 천재지변 또는 이에 따르는 불가항력으로 인하여 &quot;서비스&quot;를 제공할 수 없는 경우에는 &quot;서비스&quot; 제공에 관한 책임이 면제됩니다.</p><p id="256b42d8-17af-403c-9692-ba8318efff7d" class="">&quot;회사&quot;는 &quot;회원&quot;의 귀책사유로 인한 &quot;서비스&quot; 이용의 장애에 대하여 책임을 지지 않습니다.</p><p id="7e26ced9-6e61-4680-b179-abcac7ae5456" class="">&quot;회사&quot;는 &quot;회원&quot;이 &quot;서비스&quot;에 게재한 사실의 신뢰도, 정보나 자료의 정확성 등 내용에 관하여는 책임을 지지 않습니다.</p><p id="fda9b566-5122-44a5-bcdc-536b93ac8325" class="">&quot;회사&quot;는 &quot;서비스&quot; 이용과 관련하여 &quot;회원&quot;에게 발생한 손해 가운데 신상정보 및 전자우편 주소를 부실하게 기재하는 등 &quot;회원&quot;의 고의, 과실에 의한 손해에 대하여 책임을 지지 않습니다.</p><p id="d36fb9e7-7f5e-46d7-adb5-417482f60a83" class="">“회사”는 기간통신 사업자가 전기통신 서비스를 중지하거나 정상적으로 제공하지 아니하여 손해가 발생한 경우 책임이 면제됩니다.</p><p id="7fde5309-51d9-44db-be7d-2402276060f7" class="">“회사”는 서비스용 설비의 보수, 교체, 정기점검, 공사 등 부득이한 사유로 발생한 손해에 대한 책임이 면제됩니다.</p><p id="613146f3-eace-4edb-bba7-6d5e2ecae12d" class="">“회사”는 “회원”이 “서비스”를 이용하여 기대하는 수익을 얻지 못하거나 상실한 것에 대하여 책임을 지지 않습니다.</p><p id="657c2ebc-7984-498f-ae3b-7e76dacb23a2" class="">“회사”는 “회원”이 “서비스”를 이용하면서 얻은 자료로 인한 손해에 대하여 책임을 지지 않습니다. 또한 “회사”는 “회원”이 “서비스”를 이용하며 타 회원으로 인해 입게 되는 정신적 피해에 대하여 보상할 책임을 지지 않습니다.</p><p id="e2482319-f74c-4045-891b-c0063da2abd0" class="">“회사”는 이용자 상호간 및 이용자와 제 3자 상호 간에 서비스를 매개로 발생한 분쟁에 대해 개입할 의무가 없으며, 이로 인한 손해를 배상할 책임도 없습니다.</p><p id="471f7962-7b07-4877-81a0-aca0972db79c" class="">“회사”에서 “회원”에게 무료로 제공하는 “서비스”의 이용과 관련해서는 어떠한 손해도 책임을 지지 않습니다.</p><p id="482557a7-7b2d-4020-a3c8-b5b8abbd6e8c" class=""><strong>26. 분쟁의 해결</strong></p><p id="9cd921f9-513f-41b4-8b4f-e5c24cd944e7" class="">“회사”는 분쟁이 발생하였을 경우에 “회원”이 제기하는 정당한 의견이나 불만을 반영하여 적절하고 신속한 조치를 취합니다. 다만, 신속한 처리가 곤란한 경우에 “회사”는 “회원”에게 그 사유와 처리일정을 통보합니다.</p><p id="a0faa31d-8479-47e6-afa5-62b37774aade" class="">전항에도 불구하고, 본 약관 및 서비스이용 및 “회원”과 “회사” 관련 사항 등은 모두 대한민국 법령의 적용을 받습니다.</p><p id="3d6e3b7a-ab80-4360-8d88-0c19ca98bdd5" class="">“회원&quot;은 “회사&quot;의 &quot;서비스&quot; 이용으로 발생한 분쟁에 대해 소송이 제기될 경우 &quot;회사&quot;의 본사 소재지를 관할하는 법원을 관할법원으로 합니다.</p><p id="22123c9a-3fb7-4060-b97e-1a7818b8a0c9" class=""><strong>부칙</strong></p><p id="f89d9943-535b-41dd-a96d-828453726eaa" class="">본 약관은 2024년 9월 1일부터 적용합니다.</p><p id="a9455f51-470e-4dbd-b977-18c0a0cd8e46" class="">
</p></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>
"""