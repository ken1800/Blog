import React,{Fragment} from 'react';
import {Button,Form,FormGroup,Label,Input} from 'reactstrap'


class AddNoteForm extends React.Component{
    constructor(props){
        super(props);

        this.state ={
            title: '',
            content:'',
        }
        this.HandleChange = this.HandleChange.bind(this);
    }
    handleSubmit = (e)=>{
        e.preventDefault();
        this.props.handleSave(this.state);

        this.setState({
            title:'',
            content:''
        })
    }

    HandleChange(e){
        this.setState({
            [e.target.name] : e.target.value
        })
    }

    render(){
        return(
            <React.Fragment>
                <Form onSubmit={this.handleSubmit}>
                    <FormGroup>
                        <label>Title</label>
                        <input onChange={this.HandleChange} name='title' type='text' value={this.state.title} />
                    </FormGroup>
                    <FormGroup>
                        <label>Content</label>
                        <input onChange={this.HandleChange} name='content' type='text' value={this.state.content} />
                    </FormGroup>
                    <Button color ="success">save</Button>
                </Form>
            </React.Fragment>
        )
    }
}
export default AddNoteForm;