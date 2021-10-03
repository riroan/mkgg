import React from 'react'
import styled from 'styled-components';
import "./Recent.scss";

const Champ=()=>{
    return (
            <ChampDiv>
                <img src="http://placehold.it/50x50" alt="champ" />
                <span>리 신</span>
                <span>1승 1패 (50%)</span>
                <span>1.5/1.5/1.5(2.0)</span>
                <span>CS : 39</span>
            </ChampDiv>
    )
}

const RecentWin=()=>{
    return(
        <RecentDiv>
            <span>최근 전적</span>
            <div className="row">
                <img src="http://placehold.it/100x100" alt="recent" />
                <div className="column">
                    <span>20전 15승 5패</span>
                    <span>승률 : 75%</span>
                    <span>1.5/1.5/1.5</span>
                    <span>KDA : 2.0</span>
                </div>
            </div>
        </RecentDiv>
    )
}

const Lane = ()=>{
    return(
        <RecentLane>
            <span>선호 라인</span>
            <div className="row">
                <div className="column">
                    <img src="http://placehold.it/50x50" alt="top" />
                    <span>탑</span>
                    <span>20%</span>
                </div>
                <div className="column">
                    <img src="http://placehold.it/50x50" alt="top" />
                    <span>정글</span>
                    <span>20%</span>
                </div>
                <div className="column">
                    <img src="http://placehold.it/50x50" alt="top" />
                    <span>미드</span>
                    <span>20%</span>
                </div>
                <div className="column">
                    <img src="http://placehold.it/50x50" alt="top" />
                    <span>원딜</span>
                    <span>20%</span>
                </div>
                <div className="column">
                    <img src="http://placehold.it/50x50" alt="top" />
                    <span>서폿</span>
                    <span>20%</span>
                </div>
            </div>
        </RecentLane>
    )
}

const Badge=()=>{
    return (
        <RecentBadge>
            <span>뱃지</span>
            <BadgeSpan>퍼블러</BadgeSpan>
            <BadgeSpan>학살자</BadgeSpan>
            <BadgeSpan>딜킹</BadgeSpan>
        </RecentBadge>
    )
}

const Recent=()=> {
    return (
        <Back>
            <RecentWin />
            <ChampContainer>
                <Champ />
                <Champ />
                <Champ />
            </ChampContainer>
            <Lane />
            <Badge />
        </Back>
    )
}

export default Recent;

const BadgeSpan = styled.span`
    background-color:black;
    color:white;
`

const RecentBadge = styled.div`
    display:flex;
    flex-direction: column;
    justify-content: center;
    align-items:center;
    border : 1px solid black;
    margin:5px;
    background-color:white;
`

const RecentLane = styled.div`
    display:flex;
    flex-direction: column;
    justify-content: center;
    align-items:center;
    border : 1px solid black;
    margin:5px;
    padding:5px;
    background-color:white;
`

const RecentDiv = styled.div`
    display:flex;
    flex-direction:column;
    justify-content: center;
    align-items:center;
    padding : 5px;
    margin: 5px;
    border : 1px solid black;
    background-color:white;
    font-size:0.7rem;
`

const ChampDiv = styled.div`
    display:flex;
    flex-direction : column;
    width : 100px;
    font-size:0.8rem;
    justify-content: center;
    align-items:center;
    margin:5px;
    border: 1px solid black;
    padding : 3px;
    background-color:white;
`

const ChampContainer = styled.div`
    display:flex;
    border : 1px solid black;
    margin : 5px;
    background-color:#eee;
    padding : 3px;
`

const Back = styled.div`
    display:flex;
    justify-content: center;
    background-color:lightblue;
`