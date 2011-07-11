window.addEvent('domready', function(){
    var previous = 0;
    var operation;
    $('screen-box').focus();
    
    $$('input').each(function(el){
        if (el.type == 'button') {
            $(el).addEvent('click', function(){
                if (el.name == 'calculate') {
                    $('screen-box').value = calculate(previous, operation, Number($('screen-box').value));
                }else{
                    operation = el.name;
                    previous = Number($('screen-box').value);
                    $('screen-box').value = '';
                }
                
                $('screen-box').focus();
            });
        };
    });
});

var calculate = function(previous, operation, current){
    console.log(previous,operation,current);
    switch(operation){
        case 'multiply':
            return previous * current;
        break;
        case 'divide':
            return previous / current;
        break;
        case 'add':
            return previous + current;
        break;
        case 'subtract':
            return previous - current;
        break;
    }
};