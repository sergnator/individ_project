if(!document.cookie.includes('id='))
{
    window.location = "/view/login"
} 

const postData = async (url = '', data) => {
    // Формируем запрос
    const response = await fetch(url, {
      method: 'POST',
     
      headers: {
        'Content-Type': 'text'
      },
      body: data
    });
    return response.text()
}
postData('/username', document.cookie.split('=')[1]).then((data) => {
    document.getElementById('username').textContent = data
});


let xmr = new XMLHttpRequest()
jsons = []
xmr.open("GET", "/solutions")
xmr.onload = () =>{
    
    let lst1 = xmr.response.split('/n')
    console.log(lst1)
    lst1.forEach(element => {
        element = element.replace("'", '"')
        console.log(element)
        if(element.includes('}')){
            console.log(JSON.parse(element))
            console.log(element)
            jsons.push(JSON.parse(element))    
        }
    });
    jsons.forEach(element => {
        let div_container = document.createElement('div')
        div_container.className = 'box-content'
    
        
        let div_content = document.createElement('p')
        div_content.className = 'content'
        div_content.textContent = element.content
    
    
        let div_head = document.createElement('div')
        div_head.className = 'head-of-post'
    
        
        let div_username = document.createElement('div')
        div_username.className = 'username-of-post'
        div_username.textContent = element.date
        
        let label = document.createElement('label')
        label.className = 'date'
        label.textContent = element.username
        
        div_username.append(label)
        div_head.append(div_username)
        div_container.append(div_head)
        div_container.append(div_content)
        
        let main = document.getElementById('main')
        main.prepend(div_container)
        
        
    });

}
xmr.send()


postData('/typeofuser', document.cookie.split('=')[1]).then((data) => {
    if (data == 'student'){
        let a = document.createElement('a')
        a.href = 'newPost'
        a.className = 'newPost'
        a.textContent = 'Новый ответ'
        let m = document.getElementsByClassName('hrefs')[0]
        m.prepend(a)
    }
    else {
        let a_new_q = document.createElement('a')
        a_new_q.href = 'newQuest'
        a_new_q.className = 'newPost'
        a_new_q.textContent = 'Новое задание'

        let a_new_stud = document.createElement('a')
        a_new_stud.href = 'newStudent'
        a_new_stud.className = 'newPost'
        a_new_stud.textContent = 'Новый ученик'

        let a_solutions = document.createElement('a')
        a_solutions.href = 'main'
        a_solutions.className = 'newPost'
        a_solutions.textContent = 'Главная'

        let m = document.getElementsByClassName('hrefs')[0]
        m.prepend(a_new_q)
        m.prepend(a_new_stud)
        m.prepend(a_solutions)
    }
});

