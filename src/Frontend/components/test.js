class TwoDivs extends React.Component {
    state = {
      div1Shown: true,
    }
  
    handleButtonClick() {
      this.setState({
        div1Shown: false,
      });
    }
  
    render() {
        const changeMenu = () => {
            //const divElement = document.getElementById('Login');
      
            // Чтобы удалить все дочерние элементы дива
            //while (divElement.firstChild) {
            //divElement.removeChild(divElement.firstChild);
            //}
            // Чтобы удалить сам див
            //divElement.parentNode.removeChild(divElement);
          }
          return
      return (
        <div>
          <button onClick={() => this.handleButtonClick()}>Show div2</button>
          {
          this.state.div1Shown ? 
             (<div className="div1">Div1</div>) 
             : (<div className="div2">Div2</div>)
          }
        </div>
      );
    }
  }
  