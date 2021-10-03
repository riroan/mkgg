import React from 'react';
import Header from './component/Header';
import User from './component/User';
import Recent from './component/Recent';
import Daily from './component/Daily';
import Most from './component/Most';
import Match from './component/Match';

import styled from 'styled-components';

const App = ()=> {
  return (
    <Back>
      <Header />
      <User />
      <Recent />
      {/* <Daily /> */}
      <Match />
      <Most />
    </Back>
  );
}

export default App;

const Back = styled.div`
  width : 1000px;
  margin : 0 auto;
`