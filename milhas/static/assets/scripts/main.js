// Using the module pattern for a jQuery feature
         $(document).ready(function () {

                   $('.sidebarCollapse').on('click', function () {
                       $('#sidebar').toggleClass('active');
                       $('#container').toggleClass('index5');
                       var mq = window.matchMedia( "(max-width: 730px)" );
                          if (mq.matches) {
                              $('#menuBackground').toggleClass('hide');
                              $('#menuShare').toggleClass('hide');
                          }
                          else {
                              // window width is greater than 500px
                          }
                       //$('#navbar').toggleClass('active');
                       //$('#menuBackground').toggleClass('components');
                       //$('#menu').toggleClass('menu');

                       $('#logo-black-friday').toggleClass('img-responsive');
                       $('#arrow').toggleClass('rotate-inverse');
                       $('#view-offer').toggleClass('hide');
                       //$('.menuShare').toggleClass('hide');
                   });
                 });
                 $('.affiliates').on('click', function () {
                   if(window.location.hash.length > 0){
                            window.location = "https://www.maxmilhas.com.br/" + window.location.hash;
                            return;
                        }
                        window.location = "https://www.maxmilhas.com.br/" + window.location.search;
                 });
             function copy_code(cupom,offer){
                  ga('send', 'event', 'Black Friday', 'Cupons', cupom);
                  document.getElementById(cupom).select();
                  document.execCommand("Copy");

                  $('#copy-cupom-' + offer).toggleClass('hide',1000);
                  $('#cupom-' + offer).toggleClass('hide',1000);


             };

             function out(offer){
              $('#copy-cupom-' + offer).addClass('hide',1000);
                $('#cupom-' + offer).removeClass('hide',1000);
             };

             // Set the date we're counting down to

                  // Set the date we're counting down to
                  // var countDownDate = new Date(maxdate).getTime();

                  var sourceminDate = new Date(mindate);
                  var sourcemaxDate = new Date(maxdate);

                  sourcemaxDate.setHours(maxdate.substring(11, 13));
                  sourceminDate.setHours(mindate.substring(11, 13));

                  var maxDate = sourcemaxDate.getTime();
                  var minDate = sourceminDate.getTime();

                  var fullProgress = maxDate - minDate;

                // Update the count down every milesecond
                  var x = setInterval(function() {

                  // Get todays date and time
                  var now = new Date().getTime();

                  // Find the distance between now an the count down date
                  var distance = maxDate - now;

                  // Time calculations for days, hours, minutes and seconds
                  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                  var seconds = Math.floor((distance % (1000 * 60)) / 1000);
                  var mileseconds = Math.floor((distance % (1000 * 60)) / 1000 * 60 %100);
                  //var mileseconds = now.getMilliseconds();
                  //  2 digitis output ///
                  hours = ("0" + hours).slice(-2);
                  minutes = ("0" + minutes).slice(-2);
                  seconds = ("0" + seconds).slice(-2);
                  mileseconds = ("0" + mileseconds).slice(-2);

                    // Display the result in the element with id="demo"
                    document.getElementById("countdown").innerHTML =   hours + ":" + minutes + ":" + seconds + ":" + mileseconds ;

                    newprogress =  (distance * 100) / fullProgress;
                    //newprogress =  distance * 10000000/ countDownDate;

                    $('#theprogressbar').attr('aria-valuenow', newprogress + "%").css('width',newprogress + "%");

                    if (newprogress < 5 ) {
                     $("#theprogressbar").css({ 'background': 'Red' });
                    }

                  // If the count down is finished, write some text
                  if (distance < 0) {
                    clearInterval(x);
                    location.reload();
                    document.getElementById("countdown").innerHTML = "00:00:00:00";
                  }
                }, 100);

          $(document).on('click',function(){
            $('.collapse').collapse('hide');
          })
