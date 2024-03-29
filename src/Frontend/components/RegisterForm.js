import React from 'react';
class RegisterForm extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        email: '',
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
      console.log('Submitting:', this.state.username, this.state.email, this.state.password);
    }
  
    render() { 
      return (
        <div className="RegisterForm">
        <h1>Create Account</h1>
        <form onSubmit={this.handleSubmit}>
          <label>
            Email:
            <input type="text" name="email" value={this.state.email} onChange={this.handleChange} />
          </label>
          <br />
          <label>
            Login:
            <input type="text" name="username" value={this.state.username} onChange={this.handleChange} />
          </label>
          <br />
          <label>
            Password:
            <input type="password" name="password" value={this.state.password} onChange={this.handleChange} />
          </label>
          <br />
          <input type="submit" value="Submit" />
        </form>
        </div>
      );
    }
  }
  
  export default RegisterForm;