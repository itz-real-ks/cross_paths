
async function searchDocs() {
    const q = document.getElementById("search").value.toLowerCase();
    const resBox = document.getElementById("results");
    const idxData = await fetch("/assets/index.json").then(r=>r.json());
    resBox.innerHTML="";
    for(const p of idxData){
        if(p.content.toLowerCase().includes(q)){
            resBox.innerHTML += `<div><a href="/pages/${p.id}.html">${p.title}</a></div>`;
        }
    }
}
