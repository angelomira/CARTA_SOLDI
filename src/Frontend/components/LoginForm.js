import React from 'react';
class LoginForm extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        username: '',
        password: ''
      };
    }
  
    handleChange = (event) => {
      this.setState({
        [event.target.name]: event.target.value
      });
    }

    handleSubmit = (event) => {
      event.preventDefault();
      // Место для вставки логики отправки данных (ДЛЯ ТИМОФЕЯ)
      console.log('Submitting:', this.state.username, this.state.password);
    }

  
    render() {
      return (
        <div className="LoginForm" id="Login">
        <h1>Login</h1>
        <form onSubmit={this.handleSubmit}>
          <label>
            Login:
            <input type="text" name="username" value={this.state.username} onChange={this.handleChange} />
          </label>
          <br />
          <label>
            password:
            <input type="password" name="password" value={this.state.password} onChange={this.handleChange} />
          </label>
          <br />
          <input type="submit" value="Submit" />
        </form>
        </div>
      );
    }
  }
  
  export default LoginForm;