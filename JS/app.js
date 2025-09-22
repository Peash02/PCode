users = []
function signup(obj)
{
    users.push(obj)
    console.log('function has run');
    console.log(obj)
}

signup(
    {
        email:'example@mail.com',
        password:'pass123',
        name:'John Doe',
        discord:'disc123',
        subscription:'VIP',
        lessonCompleted:[1,2,3]
    })