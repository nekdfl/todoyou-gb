import React from 'react'


const MenuItem = ({menuitem}) => {
    return (
        <li>
            <a href="{menuitem.url}">{menuitem.name}</a>
        </li>
    )
}
const Menu = ({items = []}) => {

    return (
        <ul>
            {items.map((menuitem, key) => <MenuItem menuitem={menuitem} key={key}/>)}
        </ul>
    )
}
export default Menu