import React from 'react'
import styled, {css} from 'styled-components'
import { MdKeyboardArrowDown } from "react-icons/md";

interface divProps{
    vertical? : boolean
    margin? : boolean
    size? : boolean
    width? : boolean
}
interface teamProps{
    name: string
}

const Team=(props:teamProps)=>{
    return (
        <Div width={true}>
            <img src="http://placehold.it/15x15" alt="team" />
            {props.name}
        </Div>
    )
}

const MatchItem=()=> {
    return (
        <Back>
            <Div vertical={true}>
                <span>승리</span>
                <span>일반</span>
                <span>날짜</span>
                <span>15분</span>
            </Div>
            <Div vertical={true} margin={true} size={true}>
                <Div>
                    <img src="http://placehold.it/60x60" alt="champ" />
                    <Div vertical={true}>
                        <img src="http://placehold.it/25x25" alt="spell" />
                        <img src="http://placehold.it/25x25" alt="spell" />
                    </Div>
                    <Div vertical={true}>
                        <img src="http://placehold.it/25x25" alt="rune" />
                        <img src="http://placehold.it/25x25" alt="rune" />
                    </Div>
                </Div>
                <span>리신 레벨 15</span>
            </Div>
            <Div vertical={true} size={true}>
                <span>1.5/1.5/1.5</span>
                <span>KDA 2.0</span>
                <span>킬관여 70%</span>
                <span>cs 76(5.6)</span>
            </Div>
            <Div vertical={true} margin={true}>
                <Div>
                    <img src="http://placehold.it/20x20" alt="item" />
                    <img src="http://placehold.it/20x20" alt="item" />
                    <img src="http://placehold.it/20x20" alt="item" />
                    <img src="http://placehold.it/20x20" alt="item" />
                </Div>
                <Div>
                    <img src="http://placehold.it/20x20" alt="item" />
                    <img src="http://placehold.it/20x20" alt="item" />
                    <img src="http://placehold.it/20x20" alt="item" />
                    <img src="http://placehold.it/20x20" alt="item" />
                </Div>
            </Div>
            <Div vertical={true} size={true}>
                <img src="http://placehold.it/25x25" alt="ward" />
                <span>구매 : 1</span>
                <span>설치 : 1</span>
                <span>파괴 : 1</span>
            </Div>
            <Div>
                <Div vertical={true} size={true}>
                    <Team name="팀원"/>
                    <Team name="팀원"/>
                    <Team name="팀원"/>
                    <Team name="팀원"/>
                    <Team name="팀원"/>
                </Div>
                <Div vertical={true} size={true}>
                    <Team name="팀원"/>
                    <Team name="팀원"/>
                    <Team name="팀원"/>
                    <Team name="팀원"/>
                    <Team name="팀원"/>
                </Div>
            </Div>
            <Div vertical={true}>
                <Badge>퍼블러</Badge>
                <Badge>학살자</Badge>
                <Badge>딜킹</Badge>
                <Badge>철거왕</Badge>
            </Div>
            <Button>
                <MdKeyboardArrowDown />
            </Button>
        </Back>
    )
}

export default MatchItem


const Button = styled.button`
    display:flex;
    align-items:center;
    justify-content:center;
    box-sizing:border-box;
    width:1.8rem;
    height:1.8rem;
    font-size:3rem;
    padding:0;
    color:#1588fa;
    position:absolute;
    right:0;
    bottom:0;
    background-color:transparent;
    border-color:transparent;
`

const Badge = styled.div`
    background-color:black;
    color:white;
    font-style:bold;
    margin:1px;
`

const Div = styled.div`
    display:flex;
    justify-content: center;
    align-items:center;
    ${
        (props:divProps)=>props.vertical && css`
            flex-direction:column;
        `
    }
    ${
        (props:divProps)=>props.margin && css`
            margin: 10px;
        `
    }
    ${
        (props:divProps)=>props.size && css`
            font-size:0.7rem;
        `
    }
    ${
        (props:divProps)=>props.width && css`
            width:75px;
        `
    }
`

const Back = styled.div`
    position:relative;
    display:flex;
    justify-content: center;
    align-items:center;
    background-color:skyblue;
    padding : 20px;
    height : 100px;
    margin : 20px 5px;
    box-sizing:border-box;
`