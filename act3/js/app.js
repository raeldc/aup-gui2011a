window.addEvent('domready', function(){
    // Add new students
    $('add-button').addEvent('click', function(){
        var name = $('name-textbox').value;
        var score = $('score-textbox').value;
        if (name.length) {
            var row = new Element('tr');

            var checkboxcol = new Element('td');
            
            var checkbox = new Element('input', {
                'type': 'checkbox',
                'name': 'student-checkbox',
                'events': {
                    'click': get_average
                }
            });

            var namecol = new Element('td', {
                'html': name
            });
            
            var scorecol = new Element('td', {
                'html': score,
                'class': 'score'
            });
            
            checkboxcol.grab(checkbox);
            row.grab(checkboxcol);
            row.grab(namecol);
            row.grab(scorecol);
            
            $('students').getElement('tbody').grab(row);
        };
    });
    
    var get_average = function() {
        var item_count = 0;
        var item_sum = 0;
        $('students').getElements('input').each(function(e){
            if (e.type == 'checkbox' && e.name == 'student-checkbox' && e.checked) {
                item_count++;
                item_sum += Number($(e).getParents('tr').getElement('.score').get('text'));
            };
        });
        console.log(item_sum, item_count);
        $('average-textbox').set('text', item_sum/item_count);
    };
});