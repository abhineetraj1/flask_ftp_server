document.getElementById("upl").ondrag =k;
document.getElementById("upl").ondragover =k;
document.getElementById("upl").ondragend =k;
document.getElementById("upl").ondrop =p;
function k(e) {
	e.preventDefault();
	e.stopPropagation();
}
function p(e) {
	k(e);
	document.getElementById("upl-btn").style.display="block";
	document.getElementById("le").files=e.dataTransfer.files;
}
document.getElementsByTagName("input")[0].oninput = function () {
	console.log("Uploading");
	setInterval(mk, 1000);
}
function mk() {
	if (document.getElementsByTagName("input")[0].files != "") {
		document.getElementById("upl-btn").style.display="block";
		document.getElementById("le").files = document.getElementsByTagName("input")[0].files;
		clearInterval(mk, 1000);
		console.log("Done");
	}
}