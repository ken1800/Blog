
import React, { Component } from 'react';
import './App.css';
import { Button, Container, Row,Col } from 'reactstrap';
import ListNote from './components/ListNote';
import AddNoteForm  from './components/AddNoteForm';
import {fetchNotes,fetchNote,updateNote, addNote} from './api';
import Websocket from 'react-websocket';
import EditNoteForm from './components/EditNoteForm';


class App extends Component {
  constructor(props) {
    super(props);

    this.handleItemClick = this.handleItemClick.bind(this);
    this.handleAddNote = this.handleAddNote.bind(this);
    
    this.getData = this.getData.bind(this);
    this.handleSaveNote = this.handleSaveNote.bind(this);
    this.handleOnChange = this.handleOnChange.bind(this);
  }
  state = {

    notes:[],
    note:{},
    current_note_id:0,
    is_creating:true,
    is_fetching:true

  };
componentDidMount(){
  this.getData();
}


async getData(){
let data = await fetchNotes();
this.setState({notes:data});
}

async handleItemClick(id) {
  let selected_note = await fetchNote(id);

  this.setState((prevState) => {
    return {
      is_creating: false, 
      current_note_id: id,
      note: selected_note
    }
  })
}



handleAddNote(){
this.setState((prevState)=>{
  return {is_creating:true,}
})
}   

async handleSaveNote(data){
  await addNote(data);
  await this.getData();
}

handleData(data) {
  let result = JSON.parse(data);

  let current_note = this.state.note;
  if(current_note.id === result.id) {
    this.setState({note: result});
  }
}


handleOnChange(e) {
  let content = e.target.value;
  let current_note = this.state.note;
  current_note.content = content;

  this.setState({
    note: current_note
  });

  const socket = this.refs.socket;
  socket.state.ws.send(JSON.stringify(current_note));
}

 
  render() {
    
 
    return (
       
      <React.Fragment>
        <Container>
        <Row>
          <Col xs="10">
            <h2>Api Feed</h2>
          </Col>
          <Col xs="2">
          <Button color="primary" onClick={this.handleAddNote}>New</Button>
          </Col>
        </Row>

        <Row>
        <Col xs="4">
        <ListNote notes={this.state.notes} handleItemClick={(id)=>this.handleItemClick(id)}/>
        </Col>
        <Col>
        {
        this.state.is_creating?
        <AddNoteForm handleSave={this.handleSaveNote} />:
        <EditNoteForm handleChange={this.handleOnChange} note={this.state.note}/>
        }

<Websocket ref="socket" url='ws://127.0.0.1:8000/react'
              onMessage={this.handleData.bind(this)}/>
        </Col>
        </Row>
 
        </Container>


      </React.Fragment>
      
    );
    
  }
}

export default App; 
