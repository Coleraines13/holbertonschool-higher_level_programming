#!/usr/bin/node
$(document).ready(function () {
    const salutUri = 'https://fourtonfish.com/hellosalut/?lang=fr';

    function getSalut () {
        return $.get({
          url: salutUri,
          dataType: 'json'
        });
    }

    getSalut().then((res) => {
      $hellElement.text(res.hello);
    });
});