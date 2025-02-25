# <script>
#         // model manage
#         $(document).ready(function() {
#             // Load models on page load
#             loadModels();

#             // Function to load models via AJAX
#             function loadModels() {
#                 $.ajax({
#                     url: '/manage_models/',
#                     type: 'GET',
#                     dataType: 'json',
#                     success: function(data) {
#                         var modelListHtml = '';
#                         $.each(data.models, function(index, model) {
#                             modelListHtml += '<span class="nameModel" data-model="' + model + '">' + model +
#                                              '<span class="deleteModel" data-model="' + model + '">&times;</span></span>';
#                         });
#                         $('#modelList').html(modelListHtml);
#                     },
#                     error: function(xhr, status, error) {
#                         console.error("Failed to load models", status, error);
#                         alert('Failed to load models.');
#                     }
#                 });
#             }

#             // Add model
#             $('#addModelBtn').click(function() {
#                 var newModelName = $('#newModelName').val();
#                 if (newModelName) {
#                     $.ajax({
#                         url: '/manage_models/',
#                         type: 'POST',
#                         dataType: 'json',
#                         contentType: 'application/json',
#                         data: JSON.stringify({ action: 'add', model_name: newModelName }),
#                         success: function(data) {
#                             loadModels();
#                             $('#newModelName').val('');
#                             // Update the select element
#                             updateModelSelect(data.models);
#                         },
#                         error: function(xhr, status, error) {
#                             console.error("Failed to add model", status, error);
#                             alert('Failed to add model.');
#                         }
#                     });
#                 } else {
#                     alert('Please enter a model name.');
#                 }
#             });

#             // Delete model
#             $(document).on('click', '.deleteModel', function() {
#                 var modelToDelete = $(this).data('model');
#                 $.ajax({
#                     url: '/manage_models/',
#                     type: 'POST',
#                     dataType: 'json',
#                     contentType: 'application/json',
#                     data: JSON.stringify({ action: 'delete', model_name: modelToDelete }),
#                     success: function(data) {
#                         loadModels();
#                         // Update the select element
#                         updateModelSelect(data.models);
#                     },
#                     error: function(xhr, status, error) {
#                         console.error("Failed to delete model", status, error);
#                         alert('Failed to delete model.');
#                     }
#                 });
#             });

#             // Update the select element with new models
#             function updateModelSelect(models) {
#                 var selectElement = $('#id_model');
#                 selectElement.empty(); // Clear existing options
#                 $.each(models, function(index, model) {
#                     selectElement.append($('<option>', {
#                         value: model,
#                         text: model
#                     }));
#                 });
#             }

#             // Translate button click event
#             $(document).on('click', '.translate-btn', function() {
#                 var targetId = $(this).data('target');
#                 var preElement = $('#' + targetId);
#                 var textToTranslate = preElement.text();
#                 var transElement = $("#textTrans");
#                 var button = $(this);
#                 button.prop('disabled', true);

#                 $.ajax({
#                     url: '/translate/', // آدرس endpoint ترجمه
#                     type: 'POST',
#                     data: {
#                         'text': textToTranslate,
#                         'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
#                     },
#                     dataType: 'json',
#                     success: function(data) {
#                         transElement.html(data.translation); // جایگزین کردن متن با ترجمه
                        
#                         transElement.css('direction', 'rtl'); // راست‌چین کردن متن
#                     },
#                     error: function(xhr, status, error) {
#                         console.error("Translation failed", status, error);
#                         alert('Failed to translate.');
#                         button.text('Translate');
#                     },
#                     complete: function() {
#                         button.prop('disabled', false);
#                     }
#                 });
#                 $('#modelTranslateContainer').show();

#             });
            
        

#         $('#btnTransCopy').click(function(){
#             // گرفتن متن از تگ مورد نظر
#             var text = document.getElementById('textTrans').innerText;

#             // استفاده از Clipboard API برای کپی کردن متن
#             navigator.clipboard.writeText(text).then(function() {
#                 console.log('متن ترجمه با موفقیت کپی شد!');
#             }, function(err) {
#                 console.error('متاسفانه متن ترجمه کپی نشد: ', err);
#             });

#            var originalIcon = $(this).find('i').attr('class'); // ذخیره آیکون اصلی
#            $(this).find('i').removeClass().addClass('fa fa-check'); // تغییر به آیکون جدید
       
#            // بازگرداندن آیکون اصلی بعد از یک ثانیه
#            setTimeout(function() {
#                $(this).find('i').removeClass().addClass(originalIcon); // بازگرداندن آیکون اصلی
#            }.bind(this), 1000); // 1000 میلی‌ثانیه برابر با یک ثانیه
       
#         });


#         $(document).on('click', '.btn-copy', function() {
#             var targetId = $(this).data('target');
#             var copyElement = $('#' + targetId);
#             // گرفتن متن از تگ مورد نظر
#             var text = copyElement.text();
#             // استفاده از Clipboard API برای کپی کردن متن
#             navigator.clipboard.writeText(text).then(function() {
#                 console.log('متن با موفقیت کپی شد!');
#             }, function(err) {
#                 console.error('متاسفانه متن کپی نشد: ', err);
#             });
            
#            var originalIcon = $(this).find('i').attr('class'); // ذخیره آیکون اصلی
#            $(this).find('i').removeClass().addClass('fa fa-check'); // تغییر به آیکون جدید
       
#            // بازگرداندن آیکون اصلی بعد از یک ثانیه
#            setTimeout(function() {
#                $(this).find('i').removeClass().addClass(originalIcon); // بازگرداندن آیکون اصلی
#            }.bind(this), 1000); // 1000 میلی‌ثانیه برابر با یک ثانیه
#         });

#         $('#question-form').submit(function(event) {
#             event.preventDefault();
#             var model = $('#id_model').val();
#             var question = $('#id_question').val();
#             setTimeout(function() {
#                 $('#btn').text('Sending ...');
#                 $('#btn').prop('disabled', true);
#             }, 0);
#             $.ajax({
#                 type: 'POST',
#                 url: '/',
#                 data: {
#                     'model': model,
#                     'question': question,
#                     'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
#                 },
#                 dataType: 'json',
#                 success: function(data) {
#                     var uniqueId = 'ai-answer-' + Date.now();
#                     var resultItem = "<div class='mb-3'>" +
#                         "<span><b>Model:</b> </span>" + data.model +
#                         "  <span><b>Generation Time:</b> </span>" + data.time_elapsed + "<br>" +
#                         "<span><b>Me:</b> </span>" + question + "<br>" +
#                         "<span><b>AI:</b></span><br>" +
#                         "<div class='box-pre'>" +
#                         "<div class='d-flex justify-content-between'>"+
#                         "<button class='btn-copy' data-target=" + uniqueId + ">"+
#                         "<i class='fa fa-copy'></i>"+
#                         "</button>"+
#                         "<button class='translate-btn btn btn-success' data-target='" + uniqueId + "'>ترجمه فارسی</button>" +
#                         "</div>"
#                         +
#                         "<pre id='" + uniqueId + "'>" + data.answer + "</pre>" +
#                         "</div>" 
#                         +"<hr></div>";
#                     $("#boxAnswer").append(resultItem);
#                     $("#id_question").val('');
#                     $('#btn').text('Submit');
#                     $('#btn').prop('disabled', false);
#                 },
#                 error: function(xhr, status, error) {
#                     console.error("AJAX request failed", status, error);
#                     alert('Failed to send message.');
#                     $('#btn').text('Submit');
#                     $('#btn').prop('disabled', false);
#                 }
#             });
#             });

#             // Show Model Management Container
#             $('#manageModelsBtn').click(function() {
#                 $('#modelManagementContainer').show();
#             });

#             // Hide Model Management Container
#             $('#closeModelManagement').click(function() {
#                 $('#modelManagementContainer').hide();
#             });

#             // Show Model Management Container
#             $('#manageModelsBtn').click(function() {
#                 $('#modelManagementContainer').show();
#             });

#             // Hide Model Management Container
#             $('#closeModelManagement').click(function() {
#                 $('#modelManagementContainer').hide();
#             });

#             // Hide Model Management Container
#             $('#closeModeltrans').click(function() {
#                 $('#modelTranslateContainer').hide();
#             });

#             // Minimize/Maximize box_form
#             $('#down').click(function() {
#                 var boxForm = $('#boxForm');
#                 var boxAnswer = $('#boxAnswer');
#                 var isMinimized = boxForm.hasClass('minimized');

#                 if (isMinimized) {
#                     // Maximize
#                     boxForm.removeClass('minimized');
#                     boxAnswer.removeClass('expanded');
#                     $(this).html('<i class="fas fa-chevron-down"></i>');
#                 } else {
#                     // Minimize
#                     boxForm.addClass('minimized');
#                     boxAnswer.addClass('expanded');
#                     $(this).html('<i class="fas fa-chevron-up"></i>');
#                 }
#             });
#         });
        
#     </script>