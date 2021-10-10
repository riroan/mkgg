import React from 'react'
import styled, {css} from 'styled-components';

interface divProps{
    vertical? : boolean
    margin? : boolean
    backColor? : string
}

const Champion=()=>{
    return(
        <Div backColor={"lightblue"}>
            <span>1</span>
            <img src="http://placehold.it/70x70" alt="champ" />
            <Div vertical={true}>
                <span>킨드레드</span>
                <span>7.0/1.0/2.0</span>
                <span>75승 1패</span>
                <span>cs : 85</span>
            </Div>
            <span>99%</span>
        </Div>
    )
}

const Most=()=> {
    return (
        <Back>
            <Div>
                모스트 챔피언
            </Div>
            <Div vertical={true}>
                {/* <Div>
                    <Title>전체</Title>
                    <Title>솔로</Title>
                    <Title>자유</Title>
                </Div> */}
                <Champion />
                <Champion />
                <Champion />
                <Champion />
            </Div>
        </Back>
    )
}

export default Most;

const Title = styled.div`
    flex-grow:1;
    border: 1px solid black;
`

const Div = styled.div`
    display:flex;
    justify-content: center;
    align-items:center;
    margin:5px;
    ${
        (props:divProps)=>props.vertical && css`
            flex-direction:column;
        `
    }
    ${
        (props:divProps)=>props.margin && css`
            margin:10px;
        `
    }
    background-color: ${(props:divProps)=>props.backColor&& props.backColor};
`

const Back = styled.div`
    display:block;
    width:30%;
    background-color:orange;
    padding:20px;
    box-sizing:border-box;
    height : auto;
`