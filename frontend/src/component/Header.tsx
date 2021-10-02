import React from 'react'
import {MdSearch} from 'react-icons/md'
import styled from 'styled-components';

const Header = ()=> {
    return (
        <Back>
            <img src="http://placehold.it/200x100" alt="logo" />
            <Form>
                <Input type="text" />
                <Button type="submit">
                    <MdSearch />
                </Button>
            </Form>
        </Back>
    );
};

export default Header;

const Back = styled.div`
    background-color:yellow;
    display:flex;
    align-items:center;
`

const Form = styled.form`
    display:flex;
    align-items:center;
`

const Input = styled.input`
    display:flex;
    font-size:1.3rem;
    margin:0.2rem;
    height:2rem;
`

const Button = styled.button`
    background:white;
    color:black;
    border-radius:4px;
    padding:0.3rem;
    display:flex;
    align-items:center;
    justify-content:center;
    box-sizing:border-box;
    font-size:1.5rem;
    font-weight:700;
    width:2rem;
    height:2rem;
    margin:0.2rem;

    &:hover{
        background:rgba(255,255,255,0.9);
    }
`