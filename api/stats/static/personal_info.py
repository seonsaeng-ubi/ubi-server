data = """
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>개인정보 수집 이용 동의</title><style>
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
	
</style></head><body><article id="5a3f67e9-cc7b-4db7-acf2-16a07b3559db" class="page sans"><header><h1 class="page-title">개인정보 수집 이용 동의</h1><p class="page-description"></p></header><div class="page-body"><p id="18958263-33f7-4536-9bd6-ab911440a853" class="">
</p><table id="d7f03c77-282d-464b-a953-9f75b8caa064" class="simple-table"><tbody><tr id="51668deb-1637-4c2c-879c-c61783b25112"><td id="@cr?" class=""><strong>수집 목적</strong></td><td id="|wOg" class=""><strong>수집 항목</strong></td><td id="Dt@S" class=""><strong>보유 기간</strong></td></tr><tr id="c7bd9abd-2916-4885-bece-e4c09154649a"><td id="@cr?" class="">이용자 식별 및 본인 여부 확인<br/> <br/>계약 이행 및 약관 변경 등의 고지를 위한 연락<br/> <br/>본인의사 확인 및 민원 등의 고객 고충 처리<br/></td><td id="|wOg" class="">닉네임, 전화번호, 이메일, 소셜 인증 식별자</td><td id="Dt@S" class="">회사는 원칙적으로 이용자의 개인정보를 회원 탈퇴 또는 이용목적 달성시 지체없이 파기하고 있습니다.<br/> <br/>단, 이용자에게 개인정보 보관기간에 대해 별도의 동의를 얻은 경우, 또는 법령에서 일정 기간 정보보관 의무를 부과하는 경우에는 해당 기간 동안 개인정보를 안전하게 보관합니다.<br/></td></tr><tr id="09dfb7bb-f3fc-4edd-85d7-b0c4779c1444"><td id="@cr?" class="">서비스 방문 및 이용 기록 분석</td><td id="|wOg" class="">IP Address, 쿠키(Cookie),<br/> <br/>서비스 접속 일시, 서비스 이용기록, 고유기기 식별값, 스마트폰 단말기 정보(모델명, OS정보, 화면사이즈, 언어 및 국가정보, 디바이스 식별정보), 서비스 불량 이용 기록<br/></td><td id="Dt@S" class=""></td></tr></tbody></table><p id="d0fc92f5-05dc-4be6-bbe6-6d39c7e6a952" class=""><strong>개인정보처리방침</strong></p><p id="0b028e29-2083-451d-83ef-52239aa1e913" class=""><strong>1. 개인정보처리방침 수립 및 공개</strong></p><ul id="a09b5f63-9f97-45bf-9b04-5bcc35355e04" class="bulleted-list"><li style="list-style-type:disc">㈜효시컴퍼니(이하 “회사”)는 정보통신망 이용촉진 및 정보보호 등에 관한 법률, 개인정보보호법, 통신비밀보호법, 전기통신사업법 등 관련 법령을 준수하고 있습니다.</li></ul><ul id="cc3d784b-f169-4186-bee3-68b04273eecf" class="bulleted-list"><li style="list-style-type:disc">회사는 개인정보처리방침을 통하여 이용자 개인정보 수집항목, 이용목적, 이용자의 정보주체로서의 권리 및 회사의 개인정보 보호조치 등을 알려드립니다.</li></ul><ul id="1f620ef5-a3f3-44d6-804c-9e1478c2620c" class="bulleted-list"><li style="list-style-type:disc">회사는 이용자의 회원가입 절차에서 이용약관 및 개인정보처리방침에 대한 동의 절차를 거치고 있으며, 이용자가 “동의함” 버튼을 누르면 이용약관 및 개인정보처리방침을 충분히 읽고 동의한 것으로 간주됩니다.</li></ul><p id="328472ba-2714-45ed-81eb-768ee92d5247" class=""><strong>2. 개인정보처리방침 변경 고지의 의무</strong></p><p id="95616179-e89d-4538-b5a8-76b52fa633c1" class="">회사는 본 개인정보처리방침의 내용 추가, 삭제 및 수정이 있을 경우 개정 최소 7일 전에 ‘공지사항’을 통해 사전 공지 또는 개별 공지할 것입니다.</p><p id="af5f268b-a7ce-4154-994b-fb6f097f8727" class="">다만, 수집하는 개인정보의 항목, 이용목적의 변경 등과 같이 회원 권리의 중대한 변경이 발생할 때에는 최소 30일 전에 공지 및 통지하며, 필요할 경우 회원 동의를 다시 받을 수도 있습니다.</p><p id="2cc3083c-aaa9-4fdd-b7a5-2643e36688ff" class=""><strong>3. 개인정보의 수집 및 이용목적</strong></p><p id="b022a045-9936-439c-94cb-ddfeab2fc1c7" class="">회사는 다음 각 호의 목적을 위하여 이용자의 개인정보를 처리하고 있으며, 그 외 다른 목적으로 이용하지 않습니다.</p><ul id="226e6e23-fa55-46b6-903d-c15f2362031d" class="bulleted-list"><li style="list-style-type:disc">회원 관리 : 회원 식별 및 확인, 불량 회원의 부정 이용 방지, 회원에 대한 통지 및 공지사항 전달스 내 부정이용 방지 및 안정성 확보, 신규 서비스/기술 개발, 개인 맞춤 서비스 제공, 서비스 이용요금 청구 및 결제</li></ul><ul id="322994eb-acad-4b19-96ae-86c8e4e252e8" class="bulleted-list"><li style="list-style-type:disc">회원 상담 처리 : 회원의 상담∙불만 접수, 처리 결과 통보</li></ul><ul id="d5bd5757-e329-4df1-8f23-58d87b8a1659" class="bulleted-list"><li style="list-style-type:disc">서비스 제공 : 서비스 제공 및 서비스 품질 개선</li></ul><ul id="83211997-ba61-4499-b20f-b5c73009e7b6" class="bulleted-list"><li style="list-style-type:disc">마케팅 및 광고 홍보 : 마케팅 및 이벤트 홍보 등 광고성 정보 제공</li></ul><ul id="c56e7c76-96d4-482e-8502-5397b72032ae" class="bulleted-list"><li style="list-style-type:disc">상업적 통계 작성 및 정보 분석 : 이용자별 서비스 접속 및 이용 내역 분석</li></ul><p id="87417c9e-4ff7-4bb4-a23f-d10b94c41631" class=""><strong>4. 개인정보의 수집방법 및 항목</strong></p><ul id="45b85eb7-5c77-4f72-b516-bb912bf8bd6e" class="bulleted-list"><li style="list-style-type:disc">회사는 회원 가입 및 회사에서 제공하는 서비스 이용을 위해 필요한 최소한의 개인정보 등을 수집하고 처리합니다.</li></ul><table id="ab166474-93a5-4997-94f6-3a8af0e74641" class="simple-table"><tbody><tr id="087849c3-decb-4de5-8786-646b4574723b"><td id="jcZB" class=""><strong>수집 시기</strong></td><td id="J:ZX" class=""></td><td id="h}Zt" class=""><strong>수집 항목</strong></td><td id="HIts" class=""><strong>수집 목적</strong></td></tr><tr id="89fa3971-c607-4f9a-a775-9379838c356a"><td id="jcZB" class=""><strong>회원가입</strong></td><td id="J:ZX" class=""><strong>이메일 회원 가입</strong></td><td id="h}Zt" class="">이메일 주소, 닉네임, 비밀번호, 휴대전화번호</td><td id="HIts" class="">회원 가입</td></tr><tr id="b8606f39-6b6f-4bbf-991b-756b910941ff"><td id="jcZB" class=""></td><td id="J:ZX" class=""><strong>카카오톡 연동 회원 가입</strong></td><td id="h}Zt" class="">카카오톡 계정 이메일 주소, 닉네임, 휴대 전화번호, 생년월일, 성별</td><td id="HIts" class=""></td></tr><tr id="82f662cd-5851-44ce-ac00-1bce1b5fa9a8"><td id="jcZB" class=""></td><td id="J:ZX" class=""><strong>페이스북 연동 회원 가입</strong></td><td id="h}Zt" class="">페이스북 계정 이메일주소, 닉네임</td><td id="HIts" class=""></td></tr><tr id="2acfa0a5-1cf2-45bd-ab06-e73f7032809c"><td id="jcZB" class=""></td><td id="J:ZX" class=""><strong>애플 연동 회원 가입</strong></td><td id="h}Zt" class="">애플 계정 이메일주소, 닉네임</td><td id="HIts" class=""></td></tr><tr id="358b0db1-fca5-4964-9d5f-01fa2a6c22ce"><td id="jcZB" class=""></td><td id="J:ZX" class=""><strong>구글 연동 회원 가입</strong></td><td id="h}Zt" class="">구글 계정 이메일주소, 닉네임</td><td id="HIts" class=""></td></tr><tr id="dbe36489-7ee5-489f-88dc-ea83253286cf"><td id="jcZB" class=""></td><td id="J:ZX" class=""><strong>라인 연동 회원 가입</strong></td><td id="h}Zt" class="">라인 계정 이메일주소, 닉네임</td><td id="HIts" class=""></td></tr><tr id="5fcfa935-5830-4c74-a184-ef6357f482c0"><td id="jcZB" class=""><strong>서비스 이용</strong></td><td id="J:ZX" class=""></td><td id="h}Zt" class="">IP Address, 쿠키(Cookie), 서비스 접속 일시, 서비스 이용기록,고유기기 식별값, MAC 주소, 스마트폰 단말기 정보 (모델명, 이동통신사 정보, OS정보, 화면 사이즈, 언어 및 국가정보, 광고 ID, 디바이스 식별정보), 서비스 불량 이용 기록</td><td id="HIts" class="">서비스 제공 및 서비스 품질 개선, 서비스 내 부정이용 방지 및 안정성확보, 신규 서비스/기술 개발, 개인 맞춤 서비스 제공</td></tr><tr id="3b05b8db-d0cc-49e9-9d0e-4bc256baa813"><td id="jcZB" class=""></td><td id="J:ZX" class=""></td><td id="h}Zt" class="">이용자가 입력한 정보 및 작성한 저작물</td><td id="HIts" class=""></td></tr><tr id="715d96ff-cfee-4f0c-818d-283332d4e8f5"><td id="jcZB" class=""></td><td id="J:ZX" class=""></td><td id="h}Zt" class="">생년월일, 휴대전화번호, 통신사, 연계정보(CI)</td><td id="HIts" class=""></td></tr><tr id="93ef460c-c607-41c8-98d7-d697be552881"><td id="jcZB" class=""><strong>회원상담 ∙ 불만 접수,처리결과 통보</strong></td><td id="J:ZX" class=""><strong>이메일 회원 가입</strong></td><td id="h}Zt" class="">이메일 주소</td><td id="HIts" class="">회원 상담∙불만접수, 처리결과 통보</td></tr><tr id="0b6a118a-d74a-4ef8-a8c4-d93ac5ab008f"><td id="jcZB" class=""></td><td id="J:ZX" class=""><strong>팩스 접수</strong></td><td id="h}Zt" class="">팩스 번호</td><td id="HIts" class=""></td></tr><tr id="84ed3138-934d-425e-938e-da6f3ace7e62"><td id="jcZB" class=""></td><td id="J:ZX" class=""><strong>전화 접수</strong></td><td id="h}Zt" class="">휴대 전화번호</td><td id="HIts" class=""></td></tr><tr id="1db37e23-6442-43ca-8b21-c7f335b6d131"><td id="jcZB" class=""></td><td id="J:ZX" class=""><strong>우편 접수</strong></td><td id="h}Zt" class="">주소</td><td id="HIts" class=""></td></tr></tbody></table><p id="32b7315d-d4df-4f3a-a2d1-2cd4345d7f66" class=""><strong>5. 개인정보의 위탁처리</strong></p><ul id="2b37f156-cc90-423f-8b10-7e6048f1eeda" class="bulleted-list"><li style="list-style-type:disc">회사는 서비스 이용계약의 이행 및 원활한 개인정보 처리를 위하여 다음과 같이 개인정보처리업무를 위탁하고 있습니다.</li></ul><table id="233644ae-c24c-4cbd-aa5b-7c29bbf952f0" class="simple-table"><tbody><tr id="200bf471-7fd8-4223-b0db-768ed0826d6f"><td id="h=KX" class=""><strong>제공받는 업체 (연락처)</strong></td><td id="nBA;" class=""><strong>국가</strong></td><td id="fGD;" class=""><strong>이전 일시 및 이전 방법</strong></td><td id="g]K_" class=""><strong>이전 항목</strong></td><td id="&lt;oy:" class=""><strong>이용목적 및 보유기간</strong></td></tr><tr id="4e7381e2-6abe-4e0b-a1aa-7e15b70db1e9"><td id="h=KX" class="">Amazon Web Services, Inc.<br/>(https://aws.amazon.com/compliance/contact)<br/></td><td id="nBA;" class="">일본</td><td id="fGD;" class="">서비스 이용시마다 네트워크를 이용한 전송</td><td id="g]K_" class="">이메일 주소,<br/>닉네임, 전화번호<br/></td><td id="&lt;oy:" class="">서비스 제공을 위한 인프라 관리<br/>(회원 탈퇴시 혹은 혹은 위탁 계약 종료 시까지)<br/></td></tr></tbody></table><ul id="a729c60f-5f57-42c1-afa7-0611e5b76219" class="bulleted-list"><li style="list-style-type:disc">이용자는 회사의 개인정보보호책임자 및 담당부서를 통해 개인정보의 국외 이전을 거부할 수 있습니다. 이용자가 개인정보의 국외 이전을 거부하는 경우 회사는 해당 이용자의 개인정보를 국외 이전 대상에서 제외합니다. 다만, 이 경우 회사의 서비스 중 개인정보 국외 이전이 필수적으로 수반되는 서비스의 이용이 제한될 수 있습니다.</li></ul><p id="3ae20714-eef5-4611-9aa3-fa7a6f94f990" class=""><strong>6. 개인정보의 제3자 제공</strong></p><ul id="dc17d980-468d-4e04-a832-bf8d84842d5f" class="bulleted-list"><li style="list-style-type:disc">회사는 이용자의 동의 없이 개인정보를 제3자에게 제공하지 않습니다. 다만, 다음 각 호의 경우는 예외로 합니다.</li></ul><ul id="9e9d7658-542a-40bc-9c95-f202823f02e2" class="bulleted-list"><li style="list-style-type:disc">법률에 특별한 규정이 있거나 법령상 의무를 준수하기 위하여 불가피한 경우</li></ul><ul id="200e709b-64ac-4c86-b615-375a7e7fb6f4" class="bulleted-list"><li style="list-style-type:disc">공공기관이 법령 등에서 정하는 소관 업무의 수행을 위하여 불가피한 경우</li></ul><ul id="6f0e46e9-aef8-4500-bda3-befdb40b6238" class="bulleted-list"><li style="list-style-type:disc">정보주체 또는 그 법정대리인이 의사표시를 할 수 없는 상태에 있거나 주소불명 등으로 사전 동의를 받을 수 없는 경우로서 명백히 정보주체</li></ul><ul id="86605c5a-f27a-43c3-9a19-1578e5112a5f" class="bulleted-list"><li style="list-style-type:disc">또는 제3자의 급박한 생명, 신체, 재산의 이익을 위하여 필요하다고 인정되는 경우</li></ul><ul id="a446ab41-fec5-4ba9-b160-e3d810f12a4a" class="bulleted-list"><li style="list-style-type:disc">다음의 경우에는 관련 법령의 규정에 의하여 이용자의 동의 없이 개인정보를 목적 외 용도로 이용하거나 제3자에게 제공하는 것이 가능합니다.</li></ul><ul id="86b139a0-d4d4-4158-8a82-ab1138e1771e" class="bulleted-list"><li style="list-style-type:disc">유료서비스 제공에 따른 이용요금 정산을 위하여 필요한 경우</li></ul><ul id="5befb86e-be79-4dd3-afaa-2ea8aad88bbb" class="bulleted-list"><li style="list-style-type:disc">학술연구, 통계작성 등의 목적을 위하여 필요한 경우로서 특정 개인을 알아 볼 수 없는 형태로 개인정보를 제공하는 경우</li></ul><ul id="0ebd0f7a-2b03-41be-92d1-004762b3b368" class="bulleted-list"><li style="list-style-type:disc">범죄의 수사와 공소의 제기 및 유지를 위하여 필요한 경우</li></ul><ul id="bd4f3a09-4d1d-4b3f-b628-73cc2b9f2005" class="bulleted-list"><li style="list-style-type:disc">법원의 재판업무 수행을 위하여 필요한 경우</li></ul><p id="e8016a22-34d9-41f7-9917-9105b4ce3a8d" class=""><strong>7. 개인정보의 처리 및 보유기간</strong></p><ul id="623302fa-4984-4f0d-a15f-f9fc5df8620f" class="bulleted-list"><li style="list-style-type:disc">회사는 법령에 따른 개인정보 보유∙이용기간 또는 회사가 이용자로부터 개인정보를 수집시에 동의 받은 개인정보 보유∙이용기간 내에서 개인정보를 처리 및 보유합니다.</li></ul><ul id="8e195b00-fa3e-4265-89cc-d0f5e2078811" class="bulleted-list"><li style="list-style-type:disc">회사는 이용자가 이용약관 및 개인정보처리방침에 동의하고 회원가입을 한 경우, 회원이 서비스 이용계약을 해지하거나 회원 탈퇴시까지 회원의 개인정보를 보유합니다.</li></ul><ul id="c000663a-3c36-4ccd-b7f7-2cb9b9ddc043" class="bulleted-list"><li style="list-style-type:disc">단, 회사는 다음 각 호의 경우에는 해당 사유 종료시까지 개인정보를 보유할 수 있습니다.</li></ul><ul id="b926aa0e-8475-43f5-ac9c-8b749738ff11" class="bulleted-list"><li style="list-style-type:disc">관계 법령 위반에 따른 수사·조사 등이 진행중인 경우에는 해당 수사·조사 종료시까지</li></ul><ul id="0a827d66-7c97-4426-a449-9212403a10dc" class="bulleted-list"><li style="list-style-type:disc">사이트 등 이용에 따른 채권·채무관계 잔존시에는 해당 채권·채무관계 정산시까지</li></ul><ul id="ebf7feca-322d-467f-9679-98942e425345" class="bulleted-list"><li style="list-style-type:disc">제2항 본문에도 불구하고, 회사는 회원의 재가입 방지, 부정 이용을 차단하기 위하여 회원 탈퇴시로부터 1년간 회원의 개인정보를 보유할 수 있습니다.</li></ul><ul id="b99f5546-da42-4d0e-bb69-e9547d776efc" class="bulleted-list"><li style="list-style-type:disc">회사는 다음과 같이 관련 법령에 따라 개인정보를 보유할 수 있습니다.</li></ul><table id="0dc1dc9d-8d88-403e-87ad-b20575bee6de" class="simple-table"><tbody><tr id="36a99366-fd74-47a8-a4a1-bab17b4c7568"><td id="ByaI" class=""><strong>보관정보</strong></td><td id="bk\J" class=""><strong>보유기간</strong></td><td id="HjWu" class=""><strong>근거법령</strong></td></tr><tr id="4e440e06-beec-4ddc-ac7f-008db4a231c8"><td id="ByaI" class="">대금결제 및 재화 등의 공급에 관한 기록</td><td id="bk\J" class="">5년</td><td id="HjWu" class="">『전자상거래 등에서의 소비자보호에 관한 법률』</td></tr><tr id="6c04178d-2a7a-4a7c-8a94-f17dedcdfc79"><td id="ByaI" class="">계약 또는 청약철회 등에 관한 기록</td><td id="bk\J" class="">5년</td><td id="HjWu" class="">『전자상거래 등에서의 소비자보호에 관한 법률』</td></tr><tr id="4f91225e-3bdf-4b76-bf8f-f98f25d166e0"><td id="ByaI" class="">소비자의 불만 또는 분쟁처리에 관한 기록</td><td id="bk\J" class="">3년</td><td id="HjWu" class="">『전자상거래 등에서의 소비자보호에 관한 법률』</td></tr><tr id="1925ff65-626e-4d25-ae34-5b35e7a7d66e"><td id="ByaI" class="">표시 광고에 관한 기록</td><td id="bk\J" class="">6개월</td><td id="HjWu" class="">『전자상거래 등에서의 소비자보호에 관한 법률』</td></tr><tr id="f44aca11-628b-4acb-9d8b-c31785272677"><td id="ByaI" class="">전자금융 거래에 관한 기록</td><td id="bk\J" class="">5년</td><td id="HjWu" class="">『전자금융거래법』</td></tr><tr id="f71c6bfe-9b9b-491b-99d7-a898143146cb"><td id="ByaI" class="">웹사이트 방문 기록</td><td id="bk\J" class="">3개월</td><td id="HjWu" class="">『통신비밀보호법』</td></tr><tr id="45cfad9b-0c36-4117-998b-bee3c853b4d3"><td id="ByaI" class="">가입자전기통신일시, 개시/종료기간, 상대방 가입자번호, 사용도수</td><td id="bk\J" class="">1년</td><td id="HjWu" class="">『통신비밀보호법』</td></tr></tbody></table><p id="6248b825-706c-48f0-812c-ca4b0be86664" class=""><strong>8. 정보주체의 권리, 의무 및 행사방법</strong></p><ul id="f081555a-d202-40b7-a203-5244c55c1017" class="bulleted-list"><li style="list-style-type:disc">이용자는 언제든지 회사에 다음 각 호의 개인정보 보호 관련 권리를 행사할 수 있습니다.</li></ul><ul id="725bf274-a725-40cb-a765-428e06abffbf" class="bulleted-list"><li style="list-style-type:disc">개인정보 열람요구</li></ul><ul id="6ac2d9a6-7dbf-4a38-9a17-4b5f5db1252e" class="bulleted-list"><li style="list-style-type:disc">개인정보에 오류 등이 있을 경우 정정 요구</li></ul><ul id="2ef72b1d-6c53-4c87-9d64-7e2e629e4c66" class="bulleted-list"><li style="list-style-type:disc">개인정보 삭제요구</li></ul><ul id="7b8e2771-1cd3-403f-a399-72d2a9a99842" class="bulleted-list"><li style="list-style-type:disc">개인정보 처리정지 요구</li></ul><ul id="e00597e2-daa2-4be2-87f7-06064826d739" class="bulleted-list"><li style="list-style-type:disc">이용자의 제1항에 따른 권리 행사는 회사에 대해 서면, 전화, 전자우편, 모사전송(FAX) 등을 통하여 할 수 있으며, 회사는 이에 대해 지체없이 조치합니다.</li></ul><ul id="aa7d0487-f836-4a25-a58b-c4ebd48da10e" class="bulleted-list"><li style="list-style-type:disc">이용자는 개인정보의 오류 등에 대한 정정 또는 삭제를 요구한 경우에는 회사는 정정 또는 삭제를 완료할 때까지 당해 개인정보를 이용하거나 제공하지 않습니다.</li></ul><ul id="fbe3ea61-21db-47f9-825e-fb4b030db2b4" class="bulleted-list"><li style="list-style-type:disc">이용자는 개인정보 보호법 등 관계법령을 위반하여 회사가 처리하고 있는 정보주체 본인이나 타인의 개인정보 및 사생활을 침해하여서는 아니됩니다.</li></ul><ul id="2d4ef6b0-ec6c-4a75-ae8c-c7bdc45bc4be" class="bulleted-list"><li style="list-style-type:disc">“회사”는 만14세 미만 아동의 개인정보를 수집하고 있지 않으나, “회사”의 의도와 달리 만 14세 미만 아동이 “회사”에 개인정보를 제공하였다면, 이용자 및 법정 대리인은 언제든지 등록되어 있는 자신 혹은 당해 만 14세 미만 아동의 개인정보를 조회하거나 수정할 수 있으며 가입해지를 요청할 수도 있습니다.이용자 혹은 만 14세 미만 아동의 개인정보조회,수정을 위해서는 ‘개인정보변경’(또는 ‘회원정보수정’ 등)을 가입해지(동의철회)를 위해서는 “회원탈퇴”를 클릭하여 본인 확인 절차를 거치신 후 직접 열람, 정정 또는 탈퇴가 가능합니다. 혹은 개인정보관리책임자에게 서면, 전화 또는 이메일로 연락하시면 지체없이 조치하겠습니다.</li></ul><p id="48e4aedb-c319-4c3c-a83c-a061ecc23f3a" class=""><strong>9. 영업양도 등에 따른 개인정보의 이전</strong></p><p id="2c23173c-c43f-40fb-85c7-60673d0f569d" class="">회사는 영업의 전부 또는 일부의 양도·합병 등으로 개인정보를 다른 사람에게 이전하는 경우에는 미리 다음 각 호의 사항을 고지, 통지 또는 공지 등의 방법으로 해당 이용자에게 알려야 합니다.</p><ul id="0c1a73df-9577-4c3f-9593-862f6f6bb7a9" class="bulleted-list"><li style="list-style-type:disc">정보주체의 권리,의무 및 그 행사방법 이용자는 개인정보주체로서 다음과 같은 권리를 행사할 수 있습니다.</li></ul><ul id="5fd33395-99cf-4879-96f9-5f5647062ce3" class="bulleted-list"><li style="list-style-type:disc">개인정보를 이전하려는 사실</li></ul><ul id="63f7f01c-9f45-4adc-be00-011d7f152a36" class="bulleted-list"><li style="list-style-type:disc">개인정보를 이전 받는 자의 성명(법인의 경우에는 법인의 명칭), 주소, 전화번호 및 그 밖의 * 연락처</li></ul><ul id="9d2c28f9-4f8a-40b3-a258-b65f05842ca8" class="bulleted-list"><li style="list-style-type:disc">정보주체가 개인정보의 이전을 원하지 아니하는 경우 조치할 수 있는 방법 및 절차</li></ul><p id="21d5dd23-12ba-44a7-83ae-e220d6975024" class=""><strong>10. 개인정보의 자동 수집 장치(쿠키)의 설치, 운영 및 그 거부 방법</strong></p><ul id="3568bb74-d5f6-4f6a-ab00-856c35e95884" class="bulleted-list"><li style="list-style-type:disc">회사는 서비스 이용시 기기식별번호(디바이스 아이디 또는 IMEI)를 자동으로 수집합니다. 이용자가 기기식별번호 자동 수집에 거부하는 경우 서비스를 이용할 수 없습니다.</li></ul><ul id="85c5f35e-97f3-481c-b0df-aac30f0809d0" class="bulleted-list"><li style="list-style-type:disc">회사는 이용자에게 개별적인 맞춤서비스를 제공하기 위해 이용정보를 저장하고 수시로 불러오는 ‘쿠키(cookie)’를 사용합니다.</li></ul><ul id="c738bb85-8107-4bf2-b712-eef0209af650" class="bulleted-list"><li style="list-style-type:disc">쿠키는 사이트 등을 운영하는데 이용되는 서버(http)가 이용자의 컴퓨터 브라우저에게 보내는 소량의 정보이며 이용자들의 PC 컴퓨터내의 하드디스크에 저장되기도 합니다.</li></ul><ul id="516d727c-0a3c-465d-9b58-2ae35a0338a2" class="bulleted-list"><li style="list-style-type:disc">쿠키의 사용목적: 이용자가 방문한 각 서비스와 사이트 등에 대한 방문 및 이용형태, 인기 검색어, 보안접속 여부 등을 파악하여 이용자에게 최적화된 정보 제공을 위해 사용됩니다.</li></ul><ul id="4e17744b-6dbc-4319-96b8-60f0d04d8403" class="bulleted-list"><li style="list-style-type:disc">쿠키의 설치∙운영 및 거부</li></ul><ul id="01f16a68-db48-43c8-a60f-2c6fd3da846f" class="bulleted-list"><li style="list-style-type:disc">웹브라우저 상단의 도구 &gt; 인터넷 옵션 &gt; 개인정보 메뉴의 옵션 설정을 통해 쿠키 저장을 거부할 수 있습니다</li></ul><ul id="3cdc37c3-5229-4940-a290-043c98dfd6da" class="bulleted-list"><li style="list-style-type:disc">크롬 상단의 아이콘 “ ” &gt; 설정 &gt; 고급 설정 표시 &gt; 개인정보 섹션의 컨텐츠 설정 &gt; 쿠키 섹션에서 쿠키 저장을 거부할 수 있습니다</li></ul><ul id="a8b40384-f8fa-461d-9b72-b78e2bfb4b30" class="bulleted-list"><li style="list-style-type:disc">이용자가 쿠키 저장을 거부할 경우 회사가 제공하는 서비스 이용이 제한됩니다.</li></ul><p id="75ff7c62-8ae4-4ca7-a77e-55a7dbb1b164" class=""><strong>11. 개인정보의 기술적/관리적 보호 대책</strong></p><ul id="9adf1a97-5f18-4c9b-9f25-fe38e26983ac" class="bulleted-list"><li style="list-style-type:disc">회사는 이용자들의 개인정보를 취급함에 있어 개인정보가 분실, 도난, 누출, 변조 또는 훼손되지 않도록 안전성 확보를 위하여 다음과 같은 조치를 취하고 있습니다.</li></ul><ul id="1a860639-be5e-4081-83bd-25807915e43e" class="bulleted-list"><li style="list-style-type:disc">개인정보의 안전한 처리를 위한 내부 관리계획의 수립ㆍ시행</li></ul><ul id="2e2f1266-464c-48aa-b8f9-29c25d4db59d" class="bulleted-list"><li style="list-style-type:disc">개인정보에 대한 접근 통제 및 접근 권한의 제한 조치</li></ul><ul id="1a6dd640-350a-4297-99bd-dc915b9112ca" class="bulleted-list"><li style="list-style-type:disc">개인정보를 안전하게 저장ㆍ전송할 수 있는 암호화 기술의 적용 또는 이에 상응하는 조치</li></ul><ul id="9c85a2be-e470-403e-a7a9-dda656ac55e7" class="bulleted-list"><li style="list-style-type:disc">개인정보 침해사고 발생에 대응하기 위한 접속기록의 보관 및 위조ㆍ변조 방지를 위한 조치</li></ul><ul id="2766bb15-7490-44ba-9481-20c639a358e8" class="bulleted-list"><li style="list-style-type:disc">개인정보에 대한 보안프로그램의 설치 및 갱신</li></ul><ul id="aedade4a-83d7-4e76-be3d-6fb49be62d8c" class="bulleted-list"><li style="list-style-type:disc">개인정보의 안전한 보관을 위한 보관시설의 마련 또는 잠금장치의 설치 등 물리적 조치</li></ul><ul id="02a4727d-8196-412b-914e-2922f49e1180" class="bulleted-list"><li style="list-style-type:disc">개인정보취급자를 최소한으로 유지하고 있습니다. 개인정보를 처리하는 직원을 최소한으로 관리하며, 개인정보취급자에 대한 정기 교육, 수시 교육을 통하여 회원 개인정보 보호가 가장 중요한 가치임을 지속 강조하고 있습니다.</li></ul><p id="7d4eb435-e835-442c-9971-89fbfbfc7be0" class=""><strong>12. 개인정보의 파기절차 및 방법</strong></p><ul id="cc4db6ff-b8f3-4731-9fa1-5356d558dfd6" class="bulleted-list"><li style="list-style-type:disc">회사는 개인정보 보유기간의 경과, 처리목적 달성 등 개인정보가 불필요하게 되었을 때에는 지체 없이 해당 개인정보를 파기합니다.</li></ul><ul id="71882ade-001e-4a0b-80ce-3e6657600c43" class="bulleted-list"><li style="list-style-type:disc">이용자로부터 동의 받은 개인정보 보유기간이 경과하거나 처리목적이 달성되었음에도 불구하고 다른 법령에 따라 개인정보를 계속 보존하여야 하는 경우에는, 해당 개인정보를 별도의 데이터베이스(DB)로 옮기거나 보관장소를 달리하여 보존합니다.</li></ul><ul id="6124e330-9f75-4550-a200-eefe66812743" class="bulleted-list"><li style="list-style-type:disc">이용자의 개인정보 파기의 절차 및 방법은 다음과 같습니다.</li></ul><ul id="bd685bd5-1692-49c0-9818-4cf3b179f77b" class="bulleted-list"><li style="list-style-type:disc">파기절차 : 회사는 파기 사유가 발생한 개인정보를 선정하고, 회사의 개인정보 보호책임자의 승인을 받아 개인정보를 파기합니다.</li></ul><ul id="37d05d81-846d-47d4-8231-86bb077fd3b9" class="bulleted-list"><li style="list-style-type:disc">파기방법 : 회사는 전자적 파일 형태로 기록, 저장된 개인정보는 기록을 재생할 수 없도록 기술적 방법을 이용하여 파기하며, 종이 문서에 기록, 저장된 개인정보는 분쇄기로 분쇄하거나 소각하여 파기합니다.</li></ul><p id="4d7ddccb-abf9-4d70-aa0f-94806fe96c12" class=""><strong>13. 개인정보 관리 책임자</strong></p><p id="e1caffef-e278-4cd7-ae2d-950b14d10576" class="">회사는 개인정보 처리에 관한 업무를 총괄해서 책임지고, 개인정보 처리와 관련한 정보주체의 불만처리 및 피해구제 등을 위하여 아래와 같이 개인정보 보호책임자를 지정하고 있습니다.</p><ul id="b265ce7b-7f27-417e-811a-79b08bc58c91" class="bulleted-list"><li style="list-style-type:disc">개인정보 보호 책임자: (성명) 정우혁, (전화번호) 010-8074-1647</li></ul><p id="aa022f22-5409-4da0-b856-bf88940be7f5" class=""><strong>14. 권익침해 구제방법</strong></p><p id="44b29ac5-d2b6-49ff-8cf5-18eea768dd08" class="">이용자는 아래의 기관에 개인정보 침해에 대한 피해구제, 상담 등을 문의하실 수 있습니다.</p><ul id="c670ce22-af33-4822-a47b-3f1ca24d3203" class="bulleted-list"><li style="list-style-type:disc">개인정보 침해신고센터 (한국인터넷진흥원 운영)</li></ul><ul id="929dde0f-9406-487b-b530-c77537528ac8" class="bulleted-list"><li style="list-style-type:disc">개소관업무 : 개인정보 침해사실 신고, 상담 신청</li></ul><ul id="f8352c6b-fd77-4f35-b1eb-5f72a492e79c" class="bulleted-list"><li style="list-style-type:disc">홈페이지 : privacy.kisa.or.kr</li></ul><ul id="b7612d10-41e8-4b34-8402-abc3d790686a" class="bulleted-list"><li style="list-style-type:disc">전화 : (국번없이) 118</li></ul><ul id="08cc93d4-0c88-4faa-871b-dba7711085dc" class="bulleted-list"><li style="list-style-type:disc">주소 : (58324) 전남 나주시 진흥길 9(빛가람동 301-2) 3층 개인정보침해신고센터</li></ul><ul id="d60a5509-e252-4c70-8692-99f0805ea640" class="bulleted-list"><li style="list-style-type:disc">개인정보 분쟁조정위원회</li></ul><ul id="d0732626-2bbb-44dd-b3ea-205dc4da544c" class="bulleted-list"><li style="list-style-type:disc">소관업무 : 개인정보 분쟁조정신청, 집단분쟁조정 (민사적 해결)</li></ul><ul id="e46d9bae-6bac-4e29-adca-b661f4e60319" class="bulleted-list"><li style="list-style-type:disc">홈페이지 : www.kopico.go.kr</li></ul><ul id="6c9bade6-c997-4004-8d0c-3f2f01969389" class="bulleted-list"><li style="list-style-type:disc">전화 : (국번없이) 1833-6972</li></ul><ul id="3e7d8f4b-9ce8-4054-b737-d17b2e7fb11f" class="bulleted-list"><li style="list-style-type:disc">주소 : (03171)서울특별시 종로구 세종대로 209 정부서울청사 4층</li></ul><ul id="c37e4f55-84ea-45ea-9d9a-6f717b04cdbd" class="bulleted-list"><li style="list-style-type:disc">대검찰청 사이버범죄수사단</li></ul><ul id="43c0f0de-b6f8-4e32-8cea-42d32395815e" class="bulleted-list"><li style="list-style-type:disc">02-3480-3573 (www.spo.go.kr)</li></ul><ul id="7a2ec009-1756-4e69-bb28-88a8fd626257" class="bulleted-list"><li style="list-style-type:disc">경찰청 사이버안전국</li></ul><ul id="aeb4491b-583e-48a2-8a92-731d89af1a08" class="bulleted-list"><li style="list-style-type:disc">182 (<a href="http://http//cyberbureau.police.go.kr)">http://cyberbureau.police.go.kr)</a></li></ul><p id="c6d856ca-b9d4-4a50-a4e7-59288c92a54b" class=""><strong>15. 개인정보보호와 관련된 법규의 준수</strong></p><p id="06f5b93b-1f2f-474f-be8d-315218a7ae52" class="">회사는 한국에 설립되어 있으며, 서비스를 통하여 수집된 이용자의 개인정보는 한국에서 수집, 처리됩니다. 단, 회사는 개인정보의 처리를 위하여 대한민국 이외의 국가로 이용자의 개인정보를 이전할 수 있으며, 구체적인 내용은 개인정보 처리방침 제5조를 참고하시기 바랍니다. 회사는 다른 국가의 개인정보 관련 법규도 준수하고 있으며, 구체적인 내용은 국가별 개인정보 처리정책을 확인하시기 바랍니다.</p><p id="bd6ee26a-7664-43c7-8ded-bc80574be0fa" class="">공고일자 : 2024년 08월 01일</p><p id="eb105237-8188-416a-a3f5-d5a66d8b9db2" class="">시행일자 : 2024년 09월 01일</p></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>
"""