[GET]<br>
/api/categories/<br>
/api/categories/id<br>
[POST]<br>
/api/categories/create<br>
example of json:<br>
```
{"categories": [{
  "name": "Category 1",
  "children": [
    {
      "name": "Category 1.1",
      "children": [
        {
          "name": "Category 1.1.1",
          "children": [
            {
              "name": "Category 1.1.1.1"
            },
            {
              "name": "Category 1.1.1.2"
            },
            {
              "name": "Category 1.1.1.3"
            }
          ]
        },
        {
          "name": "Category 1.1.2",
          "children": [
            {
              "name": "Category 1.1.2.1"
            },
            {
              "name": "Category 1.1.2.2"
            },
            {
              "name": "Category 1.1.2.3"
            }
          ]
        }
      ]
    },
    {
      "name": "Category 1.2",
      "children": [
        {
          "name": "Category 1.2.1"
        },
        {
          "name": "Category 1.2.2",
          "children": [
            {
              "name": "Category 1.2.2.1"
            },
            {
              "name": "Category 1.2.2.2"
            }
          ]
        }
      ]
    }
  ]
}
]}
```