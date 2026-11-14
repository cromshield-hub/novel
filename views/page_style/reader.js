// Reader pagination and optional interactive endings. Literary text lives in contents/*/publish.
(function(){
 const src=document.getElementById('source'), reader=document.getElementById('reader');
 function createPage(n){
   const page=document.createElement('section');page.className='page';
   const area=document.createElement('div');area.className='content';
   const folio=document.createElement('div');folio.className='folio';folio.textContent=n;
   page.append(area,folio);reader.append(page);return area;
 }
 function render(){
   reader.replaceChildren();
   let area=createPage(1), n=1;
   for(const node of [...src.children]){
     const el=node.cloneNode(true); area.append(el);
     if(area.scrollHeight>area.clientHeight+1 && area.children.length>1){
       area.removeChild(el);area=createPage(++n);area.append(el);
     }
   }
 }
 function scale(){
   const w=Math.min(1.25,(window.innerWidth-32)/(128*96/25.4));
   for(const page of reader.children){page.style.zoom=w;}
 }
 reader.addEventListener('click',event=>{
   const button=event.target.closest('.reveal-button');
   if(!button)return;
   const answer=button.nextElementSibling;
   button.hidden=true;
   answer.hidden=false;
 });
 document.fonts.ready.then(()=>{render();scale()});
 window.addEventListener('resize',scale);
})();
