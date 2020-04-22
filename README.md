# mVolunteerio



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
  - [Hours-401](#schema-hours-401)
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
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>username <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>password <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>


##### Example _(generated)_

```json
{
  "username": "U1",
  "password": 12345
}
```




#### Responses


##### ▶ 200 

###### Headers
##### Server



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Server</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>



##### Date



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Date</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>



##### Content-Length



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Content-Length</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>



##### Connection



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Connection</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>




###### application/json



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>key <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>role <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
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

#### Tags

<div class="tags">
  <div class="tags__tag"></div>
</div>
</div>

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
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>x-access-token <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
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

###### Headers
##### Server



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Server</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>



##### Date



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Date</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>



##### Content-Length



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Content-Length</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>



##### Connection



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Connection</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>




###### application/json



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>hours <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>


##### Example
```json
{
  "hours": "40"
}
```
##### ▶ 401 - UNAUTHORIZED

###### Headers
_No headers specified_

###### application/json



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>message <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>


##### Example
```json
{
  "message": "Token is invalid!"
}
```

#### Tags

<div class="tags">
  <div class="tags__tag"></div>
</div>
</div>

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
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>x-access-token <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>hours <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>reason <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
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

###### Headers
##### Server



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Server</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>



##### Date



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Date</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>



##### Content-Length



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Content-Length</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>



##### Connection



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Connection</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>




###### application/json



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>confHours <strong>(required)</strong></td>
        <td>
          array(object)
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>confHours.hours <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>confHours.id <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>confHours.reason <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>msg <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>unconfHours <strong>(required)</strong></td>
        <td>
          array(object)
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>unconfHours.hours <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>unconfHours.id <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>unconfHours.reason <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
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

#### Tags

<div class="tags">
  <div class="tags__tag"></div>
</div>
</div>

### `POST` /confirmHours
<a id="op-post-confirmhours" />

> ConfirmHours







#### Request body
###### application/x-www-form-urlencoded



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>x-access-token <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>StuHrData <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
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

###### Headers
##### Server



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Server</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>



##### Date



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Date</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>



##### Content-Length



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Content-Length</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>



##### Connection



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Connection</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>




###### application/json



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>confHours <strong>(required)</strong></td>
        <td>
          array(object)
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>confHours.hours <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>confHours.id <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>confHours.reason <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>msg <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>unconfHours <strong>(required)</strong></td>
        <td>
          array(object)
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>unconfHours.hours <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>unconfHours.id <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>unconfHours.reason <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
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

#### Tags

<div class="tags">
  <div class="tags__tag"></div>
</div>
</div>

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
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>x-access-token <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
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

###### Headers
##### Server



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Server</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>



##### Date



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Date</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>



##### Content-Length



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Content-Length</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>



##### Connection



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Connection</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>




###### application/json



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Response</td>
        <td>
          array(object)
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>Response.Hours <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>Response.ID <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>Response.Location <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>Response.Name <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>Response.Sponsor <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>Response.Time <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
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

#### Tags

<div class="tags">
  <div class="tags__tag"></div>
</div>
</div>

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
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>x-access-token <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>Name <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>Date <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>Location <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>Hours <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
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

###### Headers
##### Server



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Server</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>



##### Date



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Date</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>



##### Content-Length



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Content-Length</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>



##### Connection



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Connection</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>




###### application/json



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>msg <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>


##### Example
```json
{
  "msg": "Opportunity Added"
}
```

#### Tags

<div class="tags">
  <div class="tags__tag"></div>
</div>
</div>

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
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>x-access-token <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>StuHrData <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
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

###### Headers
##### Server



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Server</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>



##### Date



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Date</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>



##### Content-Length



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Content-Length</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>



##### Connection



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Connection</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>




###### application/json



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>confHours <strong>(required)</strong></td>
        <td>
          array(object)
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>confHours.hours <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>confHours.id <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>confHours.reason <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>msg <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>unconfHours <strong>(required)</strong></td>
        <td>
          array(string)
        </td>
        <td></td>
        <td><em>Any</em></td>
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

#### Tags

<div class="tags">
  <div class="tags__tag"></div>
</div>
</div>

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
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>x-access-token <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>Filter <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
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

###### Headers
##### Server



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Server</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>



##### Date



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Date</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>



##### Content-Length



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Content-Length</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>



##### Connection



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Connection</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>




###### application/json



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Response</td>
        <td>
          array(object)
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>Response.Hours <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>Response.ID <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>Response.Name <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>Response.StuId <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
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

#### Tags

<div class="tags">
  <div class="tags__tag"></div>
</div>
</div>

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
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>x-access-token <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
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

###### Headers
##### Server



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Server</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>



##### Date



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Date</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>



##### Content-Length



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Content-Length</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>



##### Connection



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Connection</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>




###### application/json



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Response</td>
        <td>
          array(object)
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>Response.ID <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>Response.Name <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>Response.Time <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
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

#### Tags

<div class="tags">
  <div class="tags__tag"></div>
</div>
</div>

## Schemas

<a id="schema-login" />

#### Login

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>key <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>role <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
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

#### Hours-401

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>message <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
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
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>hours <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
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
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>confHours <strong>(required)</strong></td>
        <td>
          array(object)
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>confHours.hours <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>confHours.id <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>confHours.reason <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>msg <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>unconfHours <strong>(required)</strong></td>
        <td>
          array(object)
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>unconfHours.hours <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>unconfHours.id <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>unconfHours.reason <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
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
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>hours <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>id <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>reason <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
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
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>hours <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>id <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>reason <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
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
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>confHours <strong>(required)</strong></td>
        <td>
          array(object)
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>confHours.hours <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>confHours.id <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>confHours.reason <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>msg <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>unconfHours <strong>(required)</strong></td>
        <td>
          array(object)
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>unconfHours.hours <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>unconfHours.id <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>unconfHours.reason <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
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
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Hours <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>ID <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>Location <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>Name <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>Sponsor <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>Time <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
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
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>msg <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
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
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>confHours <strong>(required)</strong></td>
        <td>
          array(object)
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>confHours.hours <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>confHours.id <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>confHours.reason <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>msg <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>unconfHours <strong>(required)</strong></td>
        <td>
          array(string)
        </td>
        <td></td>
        <td><em>Any</em></td>
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
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Hours <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>ID <strong>(required)</strong></td>
        <td>
          integer
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>Name <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>StuId <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
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
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>ID <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>Name <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>Time <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
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
