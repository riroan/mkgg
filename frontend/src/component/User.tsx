import React from 'react'
import styled from 'styled-components';
import Rank from './Rank';

const User=()=> {
    return (
        <Back>
            <div>
                <Img src="http://placehold.it/150x150" alt="icon" />
                <Button>전적 갱신</Button>
            </div>
            <div>
                <UserInfo>소환사 이름 : </UserInfo>
                <UserInfo>소환사 레벨 : </UserInfo>
            </div>
            <Rank />
            <Rank />
        </Back>
    )
}

export default User;

const UserInfo = styled.span`
    display : block;
    margin : 10px;
`

const Img = styled.img`
    margin:5px;
`

const Back = styled.div`
    display:flex;
    background-color: cyan;
    padding : 5px;
`

const Button = styled.button`
    width : 150px;
    display: block;
    margin : 5px;
    padding : 3px;
`