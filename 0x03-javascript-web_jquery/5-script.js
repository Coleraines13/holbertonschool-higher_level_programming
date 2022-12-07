#!/usr/bin/node
const $listElem = $('ul.my_list');
const $addItemElem = $('div#add_item');

$addItemElem.on('click', () => {
    $listElem.append('<li>Item</>');
});