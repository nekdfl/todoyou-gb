import React from 'react'

const UserItem = ({user}) => {
    return (
        <tr>
            <td>
                {user.username}
            </td>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.email}
            </td>
        </tr>
    )
}
const UserList = ({items}) => {
    return (
        <table border="1">
            <thead>
                <tr>
                    <th>
                        User name
                    </th>
                    <th>
                        First name
                    </th>
                    <th>
                        Last name
                    </th>
                    <th>
                        email
                    </th>
                </tr>
            </thead>
            <tbody>
                {items.map((user) => <UserItem user={user} key={user.id}/>)}
            </tbody>
        </table>
    )
}
export default UserList