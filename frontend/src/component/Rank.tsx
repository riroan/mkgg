import React from 'react'
import styled, {css} from 'styled-components';

interface contentProps{
    content: boolean;
};

const Rank=() => {
    return (
        <Box>
            <Title>랭크게임</Title>
            <Inner content={false}>
                <Img src="http://placehold.it/125x125" alt="tier" />
                <Inner content={true}>
                    <Span>골드 4 (48p)</Span>
                    <Span>300승 300패(50%)</Span>
                </Inner>
            </Inner>
        </Box>
    )
};

export default Rank;

const Inner = styled.div`
    display : flex;
    justify-content:center;
    align-content:center;
    ${(props:contentProps)=>props.content &&
    css`
        margin:5px;
        flex-direction : column;
    `}
`

const Img = styled.img`
    margin:10px;
`

const Title = styled.span`
    margin : 1rem;
`

const Span = styled.span`
    text-align : center;
    font-size:0.7rem;
    margin:5px;
`

const Box = styled.div`
    display:flex;
    justify-content: center;
    align-items:center;
    flex-direction : column;
    background-color:white;
    width:300px;
    border: 1px solid black;
    margin : 2px;
    padding: 3px;
`