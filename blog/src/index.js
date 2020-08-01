import React from 'react';
import ReactDom from 'react-dom';
import './index.css';

function Hello(){
    return(
        <h1>Hello World</h1>
    )
}


ReactDom.render(<Hello/>,document.getElementById('root'));