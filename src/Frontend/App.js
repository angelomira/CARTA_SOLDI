import React from 'react';
import LoginForm from './components/LoginForm';
import RegisterForm from './components/RegisterForm';
import './App.css';

class App extends React.Component {
  state = {
    RegisterShown: false,
  };

  toggleRegister = () => {
    this.setState(prevState => ({
      RegisterShown: !prevState.RegisterShown
    }));
  };

  render() {
    return (
      <div className="App">
        {this.state.RegisterShown ? (
          <RegisterForm />
        ) : (
          <LoginForm />
        )}
        <button onClick={this.toggleRegister}>
          {this.state.RegisterShown ? 'Login' : 'Register'}
        </button>
      </div>
    );
  }
}

export default App;