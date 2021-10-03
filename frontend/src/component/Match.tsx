import React from 'react'
import MatchItem from './MatchItem'
import styled from 'styled-components'

const More=()=>{
    return (
        <Div>
            <Button>  
                더보기
            </Button>
        </Div>
    )
}

const Match=()=> {
    return (
        <Back>
            <MatchItem />
            <MatchItem />
            <MatchItem />
            <MatchItem />
            <More />
        </Back>
    )
}

export default Match

const Div = styled.div`
    background-color:gray;
    margin:10px 5px;
    height:50px;
`

const Button = styled.button`
    display:flex;
    justify-content: center;
    align-items: center;
    background-color:transparent;
    border-color:transparent;
    width:100%;
    height:100%;
    font-size:1.5rem;
`

const Back = styled.div`
    display:inline-block;
    background-color:magenta;
    width:70%;
    padding : 0 10px;
    box-sizing:border-box;
`