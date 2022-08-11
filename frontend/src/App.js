import logo from './logo.svg';
import './App.css';
import React from "react";
import UserList from "./components/UserList";
import Footer from "./components/Footer";
import axios from "axios";
import Menu from "./components/Menu";




class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'menu' : [
                {"name" : "menu1", "url" : "#"},
                {"name" : "menu2", "url" : "#"}
            ]
        }
    }

    componentDidMount() {


        axios.get('http://localhost:8000/api/user/')
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error))



    }

    render() {
        return (
            <div>
                <Menu items={this.state.menu}/>
                <UserList items={this.state.users}/>
                <Footer />
            </div>
        )
    }
}

export default App;
