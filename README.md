# mVolunteerio Web API

## Table of Contents

* [Servers](#servers)
* [Paths](#paths)
  - [`POST` /login](#op-post-login) 
  - [`POST` /hours](#op-post-hours) 
  - [`POST` /addhours](#op-post-addhours) 
  - [`POST` /confirmHours](#op-post-confirmhours) 
  - [`POST` /Opps](#op-post-opps) 
  - [`POST` /AddOpp](#op-post-addopp) 
  - [`POST` /deleteHours](#op-post-deletehours) 
  - [`POST` /StudentsList](#op-post-studentslist) 
  - [`POST` /MyOpps](#op-post-myopps) 
* [Schemas](#schemas)
  - [Login](#schema-login)
  - [Hours](#schema-hours)
  - [AddHours](#schema-addhours)
  - [ConfHour](#schema-confhour)
  - [UnconfHour](#schema-unconfhour)
  - [ConfirmHours](#schema-confirmhours)
  - [ListOpp](#schema-listopp)
  - [AddOpp](#schema-addopp)
  - [DeleteHours](#schema-deletehours)
  - [StudentsList](#schema-studentslist)
  - [MyOpp](#schema-myopp)


<a id="servers" />
## Servers

<table>
  <thead>
    <tr>
      <th>URL</th>
      <th>Description</th>
    <tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="http://73.57.34.161" target="_blank">http://73.57.34.161</a></td>
      <td></td>
    </tr>
  </tbody>
</table>


## Paths


### `POST` /login
<a id="op-post-login" />

> Login

#### Request body
###### application/x-www-form-urlencoded



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>username <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>password <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
  </tbody>
</table>


##### Example

```json
{
  "username": "U1",
  "password": 12345
}
```




#### Responses


##### ▶ 200 
###### application/json



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>key</td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>role</td>
        <td>
          string
        </td>
        <td></td>
      </tr>
  </tbody>
</table>


##### Example
```json
{
  "key": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTU4NzUxNzg5MSwiZXhwIjoxNTg3NTIxNDkxfQ.eyJpZCI6MX0.0FJumAKpzbBBpXHFWTAu9P7Qb3ISi4DyaD7AFcRE3dNWyp2XTlal2dlRJyjdWXZOjKIY2IPsUnOJjbghwGrlZg",
  "role": "student"
}
```


### `POST` /hours
<a id="op-post-hours" />

> Hours







#### Request body
###### application/x-www-form-urlencoded



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>x-access-token <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
  </tbody>
</table>


##### Example _(generated)_

```json
{
  "x-access-token": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTU4NzUxOTU3NSwiZXhwIjoxNTg3NTIzMTc1fQ.eyJpZCI6MX0.jNucXtDjSSO17L62u5QgWKsYpz1fqf8bBurTjwihzS5PDkr8us09Lz9YtOAlx8Z_6fVVaZWy6ErHUaIe-bt45w"
}
```




#### Responses


##### ▶ 200 
###### application/json



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>hours</td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
  </tbody>
</table>


##### Example
```json
{
  "hours": "40"
}
```




### `POST` /addhours
<a id="op-post-addhours" />

> AddHours







#### Request body
###### application/x-www-form-urlencoded



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>x-access-token <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>hours <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>reason <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
  </tbody>
</table>


##### Example _(generated)_

```json
{
  "x-access-token": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTU4NzUxOTU3NSwiZXhwIjoxNTg3NTIzMTc1fQ.eyJpZCI6MX0.jNucXtDjSSO17L62u5QgWKsYpz1fqf8bBurTjwihzS5PDkr8us09Lz9YtOAlx8Z_6fVVaZWy6ErHUaIe-bt45w",
  "hours": 20,
  "reason": "I Can"
}
```




#### Responses


##### ▶ 200 






###### application/json



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>confHours</td>
        <td>
          array(object)
        </td>
        <td></td>
      </tr>
      <tr>
        <td>confHours.hours</td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>confHours.id</td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>confHours.reason</td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>msg</td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>unconfHours</td>
        <td>
          array(object)
        </td>
        <td></td>
      </tr>
      <tr>
        <td>unconfHours.hours</td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>unconfHours.id</td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>unconfHours.reason</td>
        <td>
          string
        </td>
        <td></td>
      </tr>
  </tbody>
</table>


##### Example
```json
{
  "confHours": [
    {
      "hours": 10,
      "id": 1,
      "reason": "Grggrg"
    },
    {
      "hours": 10,
      "id": 2,
      "reason": "A"
    },
    {
      "hours": 10,
      "id": 3,
      "reason": "B"
    },
    {
      "hours": 10,
      "id": 7,
      "reason": "Hours"
    }
  ],
  "msg": "Hours added",
  "unconfHours": [
    {
      "hours": 20,
      "id": 8,
      "reason": "I Can"
    }
  ]
}
```


> ConfirmHours







#### Request body
###### application/x-www-form-urlencoded



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>x-access-token <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>StuHrData <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
  </tbody>
</table>


##### Example _(generated)_

```json
{
  "x-access-token": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTU4NzUxOTY5NSwiZXhwIjoxNTg3NTIzMjk1fQ.eyJpZCI6Mn0.2W7TWYcHFqGnm03iWyYZY_jksAlhkRj3AZpRcbbQV6UPDRYzlBhB1DgCzmjXzdtQLcLo_ljYa0bP3E118qi8xg",
  "StuHrData": "1, 9"
}
```




#### Responses


##### ▶ 200 






###### application/json



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>confHours</td>
        <td>
          array(object)
        </td>
        <td></td>
      </tr>
      <tr>
        <td>confHours.hours</td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>confHours.id</td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>confHours.reason</td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>msg</td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>unconfHours</td>
        <td>
          array(object)
        </td>
        <td></td>
      </tr>
      <tr>
        <td>unconfHours.hours</td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>unconfHours.id</td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>unconfHours.reason</td>
        <td>
          string
        </td>
        <td></td>
      </tr>
  </tbody>
</table>


##### Example
```json
{
  "confHours": [
    {
      "hours": 10,
      "id": 1,
      "reason": "Grggrg"
    },
    {
      "hours": 10,
      "id": 2,
      "reason": "A"
    },
    {
      "hours": 10,
      "id": 3,
      "reason": "B"
    },
    {
      "hours": 10,
      "id": 7,
      "reason": "Hours"
    },
    {
      "hours": 20,
      "id": 9,
      "reason": "I Can"
    }
  ],
  "msg": "Hours Confirmed",
  "unconfHours": [
    {
      "hours": 20,
      "id": 8,
      "reason": "I Can"
    }
  ]
}
```



### `POST` /Opps
<a id="op-post-opps" />

> List Opps







#### Request body
###### application/x-www-form-urlencoded



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>x-access-token <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
  </tbody>
</table>


##### Example _(generated)_

```json
{
  "x-access-token": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTU4NzUxOTY5NSwiZXhwIjoxNTg3NTIzMjk1fQ.eyJpZCI6Mn0.2W7TWYcHFqGnm03iWyYZY_jksAlhkRj3AZpRcbbQV6UPDRYzlBhB1DgCzmjXzdtQLcLo_ljYa0bP3E118qi8xg"
}
```




#### Responses


##### ▶ 200 






###### application/json



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Response</td>
        <td>
          array(object)
        </td>
        <td></td>
      </tr>
      <tr>
        <td>Response.Hours</td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>Response.ID</td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>Response.Location</td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>Response.Name</td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>Response.Sponsor</td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>Response.Time</td>
        <td>
          string
        </td>
        <td></td>
      </tr>
  </tbody>
</table>


##### Example _(generated)_

```json
[
  {
    "Hours": 10,
    "ID": "1",
    "Location": "Beach",
    "Name": "Beach cleanup",
    "Sponsor": "User, User 3",
    "Time": "09/20/2023, 00:00"
  }
]
```



### `POST` /AddOpp
<a id="op-post-addopp" />

> Add Opp







#### Request body
###### application/x-www-form-urlencoded



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>x-access-token <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>Name <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>Date <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>Location <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>Hours <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
  </tbody>
</table>


##### Example _(generated)_

```json
{
  "x-access-token": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTU4NzUxOTY5NSwiZXhwIjoxNTg3NTIzMjk1fQ.eyJpZCI6Mn0.2W7TWYcHFqGnm03iWyYZY_jksAlhkRj3AZpRcbbQV6UPDRYzlBhB1DgCzmjXzdtQLcLo_ljYa0bP3E118qi8xg",
  "Name": "Beach Cleanup",
  "Date": "2020-09-20T10:10:00",
  "Location": "Beach",
  "Hours": 10
}
```




#### Responses


##### ▶ 200 






###### application/json



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>msg</td>
        <td>
          string
        </td>
        <td></td>
      </tr>
  </tbody>
</table>


##### Example
```json
{
  "msg": "Opportunity Added"
}
```



### `POST` /deleteHours
<a id="op-post-deletehours" />

> Delete Hours







#### Request body
###### application/x-www-form-urlencoded



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>x-access-token <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>StuHrData <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
  </tbody>
</table>


##### Example _(generated)_

```json
{
  "x-access-token": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTU4NzUxOTY5NSwiZXhwIjoxNTg3NTIzMjk1fQ.eyJpZCI6Mn0.2W7TWYcHFqGnm03iWyYZY_jksAlhkRj3AZpRcbbQV6UPDRYzlBhB1DgCzmjXzdtQLcLo_ljYa0bP3E118qi8xg",
  "StuHrData": "1, 8"
}
```




#### Responses


##### ▶ 200 
###### application/json



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>confHours</td>
        <td>
          array(object)
        </td>
        <td></td>
      </tr>
      <tr>
        <td>confHours.hours</td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>confHours.id</td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>confHours.reason</td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>msg</td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>unconfHours</td>
        <td>
          array(string)
        </td>
        <td></td>
      </tr>
  </tbody>
</table>


##### Example
```json
{
  "confHours": [
    {
      "hours": 10,
      "id": 1,
      "reason": "Grggrg"
    },
    {
      "hours": 10,
      "id": 2,
      "reason": "A"
    },
    {
      "hours": 10,
      "id": 3,
      "reason": "B"
    },
    {
      "hours": 10,
      "id": 7,
      "reason": "Hours"
    },
    {
      "hours": 20,
      "id": 9,
      "reason": "I Can"
    }
  ],
  "msg": "Hours Removed",
  "unconfHours": []
}
```



### `POST` /StudentsList
<a id="op-post-studentslist" />

> StudentsList







#### Request body
###### application/x-www-form-urlencoded



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>x-access-token <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>Filter <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
  </tbody>
</table>


##### Example _(generated)_

```json
{
  "x-access-token": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTU4NzUxOTY5NSwiZXhwIjoxNTg3NTIzMjk1fQ.eyJpZCI6Mn0.2W7TWYcHFqGnm03iWyYZY_jksAlhkRj3AZpRcbbQV6UPDRYzlBhB1DgCzmjXzdtQLcLo_ljYa0bP3E118qi8xg",
  "Filter": "U"
}
```




#### Responses


##### ▶ 200 
###### application/json



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Response</td>
        <td>
          array(object)
        </td>
        <td></td>
      </tr>
      <tr>
        <td>Response.Hours</td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>Response.ID</td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>Response.Name</td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>Response.StuId</td>
        <td>
          string
        </td>
        <td></td>
      </tr>
  </tbody>
</table>


##### Example _(generated)_

```json
[
  {
    "Hours": "60",
    "ID": 1,
    "Name": "User, User 1",
    "StuId": "1111111"
  }
]
```



### `POST` /MyOpps
<a id="op-post-myopps" />

> MyOpps







#### Request body
###### application/x-www-form-urlencoded



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>x-access-token <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
  </tbody>
</table>


##### Example _(generated)_

```json
{
  "x-access-token": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTU4NzUxOTY5NSwiZXhwIjoxNTg3NTIzMjk1fQ.eyJpZCI6Mn0.2W7TWYcHFqGnm03iWyYZY_jksAlhkRj3AZpRcbbQV6UPDRYzlBhB1DgCzmjXzdtQLcLo_ljYa0bP3E118qi8xg"
}
```




#### Responses


##### ▶ 200 
###### application/json



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Response</td>
        <td>
          array(object)
        </td>
        <td></td>
      </tr>
      <tr>
        <td>Response.ID</td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>Response.Name</td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>Response.Time</td>
        <td>
          string
        </td>
        <td></td>
      </tr>
  </tbody>
</table>


##### Example _(generated)_

```json
[
  {
    "ID": "2",
    "Name": "Beach Cleanup",
    "Time": "Sun, 20 Sep 2020 10:10:00 GMT"
  }
]
```



## Schemas

<a id="schema-login" />

#### Login

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>key <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>role <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
  </tbody>
</table>

##### Example

```json
{
  "key": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTU4NzUxNzg5MSwiZXhwIjoxNTg3NTIxNDkxfQ.eyJpZCI6MX0.0FJumAKpzbBBpXHFWTAu9P7Qb3ISi4DyaD7AFcRE3dNWyp2XTlal2dlRJyjdWXZOjKIY2IPsUnOJjbghwGrlZg",
  "role": "student"
}
```
<a id="schema-hours-401" />

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>message <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
  </tbody>
</table>

##### Example

```json
{
  "message": "Token is invalid!"
}
```
<a id="schema-hours" />

#### Hours

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>hours <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
  </tbody>
</table>

##### Example

```json
{
  "hours": "40"
}
```
<a id="schema-addhours" />

#### AddHours

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>confHours <strong>(required)</strong></td>
        <td>
          array(object)
        </td>
        <td></td>
      </tr>
      <tr>
        <td>confHours.hours <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>confHours.id <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>confHours.reason <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>msg <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>unconfHours <strong>(required)</strong></td>
        <td>
          array(object)
        </td>
        <td></td>
      </tr>
      <tr>
        <td>unconfHours.hours <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>unconfHours.id <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>unconfHours.reason <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
  </tbody>
</table>

##### Example

```json
{
  "confHours": [
    {
      "hours": 10,
      "id": 1,
      "reason": "Grggrg"
    },
    {
      "hours": 10,
      "id": 2,
      "reason": "A"
    },
    {
      "hours": 10,
      "id": 3,
      "reason": "B"
    },
    {
      "hours": 10,
      "id": 7,
      "reason": "Hours"
    }
  ],
  "msg": "Hours added",
  "unconfHours": [
    {
      "hours": 20,
      "id": 8,
      "reason": "I Can"
    }
  ]
}
```
<a id="schema-confhour" />

#### ConfHour

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>hours <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>id <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>reason <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
  </tbody>
</table>

##### Example

```json
{
  "hours": 10,
  "id": 1,
  "reason": "Grggrg"
}
```
<a id="schema-unconfhour" />

#### UnconfHour

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>hours <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>id <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>reason <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
  </tbody>
</table>

##### Example

```json
{
  "hours": 20,
  "id": 8,
  "reason": "I Can"
}
```
<a id="schema-confirmhours" />

#### ConfirmHours

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>confHours <strong>(required)</strong></td>
        <td>
          array(object)
        </td>
        <td></td>
      </tr>
      <tr>
        <td>confHours.hours <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>confHours.id <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>confHours.reason <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>msg <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>unconfHours <strong>(required)</strong></td>
        <td>
          array(object)
        </td>
        <td></td>
      </tr>
      <tr>
        <td>unconfHours.hours <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>unconfHours.id <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>unconfHours.reason <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
  </tbody>
</table>

##### Example

```json
{
  "confHours": [
    {
      "hours": 10,
      "id": 1,
      "reason": "Grggrg"
    },
    {
      "hours": 10,
      "id": 2,
      "reason": "A"
    },
    {
      "hours": 10,
      "id": 3,
      "reason": "B"
    },
    {
      "hours": 10,
      "id": 7,
      "reason": "Hours"
    },
    {
      "hours": 20,
      "id": 9,
      "reason": "I Can"
    }
  ],
  "msg": "Hours Confirmed",
  "unconfHours": [
    {
      "hours": 20,
      "id": 8,
      "reason": "I Can"
    }
  ]
}
```
<a id="schema-listopp" />

#### ListOpp

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Hours <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>ID <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>Location <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>Name <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>Sponsor <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>Time <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
  </tbody>
</table>

##### Example

```json
{
  "Hours": 10,
  "ID": "1",
  "Location": "Beach",
  "Name": "Beach cleanup",
  "Sponsor": "User, User 3",
  "Time": "09/20/2023, 00:00"
}
```
<a id="schema-addopp" />

#### AddOpp

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>msg <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
  </tbody>
</table>

##### Example

```json
{
  "msg": "Opportunity Added"
}
```
<a id="schema-deletehours" />

#### DeleteHours

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>confHours <strong>(required)</strong></td>
        <td>
          array(object)
        </td>
        <td></td>
      </tr>
      <tr>
        <td>confHours.hours <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>confHours.id <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>confHours.reason <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>msg <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>unconfHours <strong>(required)</strong></td>
        <td>
          array(string)
        </td>
        <td></td>
      </tr>
  </tbody>
</table>

##### Example

```json
{
  "confHours": [
    {
      "hours": 10,
      "id": 1,
      "reason": "Grggrg"
    },
    {
      "hours": 10,
      "id": 2,
      "reason": "A"
    },
    {
      "hours": 10,
      "id": 3,
      "reason": "B"
    },
    {
      "hours": 10,
      "id": 7,
      "reason": "Hours"
    },
    {
      "hours": 20,
      "id": 9,
      "reason": "I Can"
    }
  ],
  "msg": "Hours Removed",
  "unconfHours": []
}
```
<a id="schema-studentslist" />

#### StudentsList

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Hours <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>ID <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
      </tr>
      <tr>
        <td>Name <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>StuId <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
  </tbody>
</table>

##### Example

```json
{
  "Hours": "60",
  "ID": 1,
  "Name": "User, User 1",
  "StuId": "1111111"
}
```
<a id="schema-myopp" />

#### MyOpp

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>ID <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>Name <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
      <tr>
        <td>Time <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
      </tr>
  </tbody>
</table>

##### Example

```json
{
  "ID": "2",
  "Name": "Beach Cleanup",
  "Time": "Sun, 20 Sep 2020 10:10:00 GMT"
}
```
