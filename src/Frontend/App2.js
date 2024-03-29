import React from 'react';
import LoginForm from './components/LoginForm';
import RegisterForm from './components/RegisterForm';
//import './App.css';

function App() {
  this.state = {
    RegisterShown: false,
  }
  function RegisterOrLogin(props) {
    this.setState({
      RegisterShown: this.props,
    });
    }
  return (
    <div className="App">
    this.state.RegisterShown ? 
    <RegisterForm /><button onClick={RegisterOrLogin(true)}>Register</button>
    : <LoginForm /><button onClick={RegisterOrLogin(false)}>Login</button>
    </div>
  );
}

export default App;
