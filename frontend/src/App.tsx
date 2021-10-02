import React from 'react';
import Header from './component/Header'
import User from './component/User'

import styled from 'styled-components';

const App = ()=> {
  return (
    <Body>
      <Header />
      <User />
    </Body>
  );
}

export default App;

const Body = styled.div`
  margin:0;
  padding:0
`