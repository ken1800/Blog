
const url = 'http://localhost:8000/react';

export const fetchNotes = async ()=>{
    return fetch(url,{})
    .then(res=>res.json())
    .then(data=>{
        return data;
    });
}
export const fetchNote = (id) => {
    return fetch(`${'http://localhost:8000/react/' + id}`, {})
      .then(res => res.json())
      .then(data => {
        return data;
      });
  }
  

export const addNote =(note)=>{
    fetch(url,{
       method: 'POST',
       headers:{
           Accept:'application/json',
           'Content-Type':'application/json'
       } ,
       body:JSON.stringify(note)
    })
    .then(res=>res.json())
    .then(data=>{
    })
    return note;
}

export const updateNote =(note)=>{
    console.log('we are updating');
    console.log('update a note with id',note.id);
}