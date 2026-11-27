/**
 * Tạo Google Form khảo sát "Xem trước slide bài giảng trên LMS" — đúng 11 câu ở evidence/survey/questions.md.
 *
 * Cách chạy (3 phút):
 *   1. Mở https://script.google.com → New project (Dự án mới).
 *   2. Xoá hết code mẫu, dán toàn bộ file này vào, bấm Save (Lưu).
 *   3. Chọn hàm createSurvey → bấm Run (Chạy) → cấp quyền cho tài khoản Google của bạn.
 *   4. Mở View → Logs (Nhật ký thực thi): có 3 link — link GỬI cho mọi người, link SỬA form, link Sheet kết quả.
 *
 * Form KHÔNG thu email. Câu 11 (liên hệ) là tuỳ chọn — khi xuất results.csv phải XOÁ cột này trước khi commit.
 */
function createSurvey() {
  var form = FormApp.create('Khảo sát: xem trước slide bài giảng trên LMS (AI20K K5)');
  form.setDescription(
    'Nhóm MHTeam (L3B) đang làm hackathon về việc xem trước slide bài giảng trên LMS. ' +
    'Form mất khoảng 2 phút, ẩn danh, chỉ hỏi về những lần bạn đã thực sự xem slide. Cảm ơn bạn!');
  form.setCollectEmail(false);
  form.setProgressBar(true);
  form.setConfirmationMessage('Cảm ơn bạn đã trả lời! 🙏');

  // ---- Phần 1 ----
  form.addMultipleChoiceItem()
    .setTitle('1. Bạn là:')
    .setChoiceValues(['Học viên L3A', 'Học viên L3B', 'Lab coach / TA', 'Khác'])
    .setRequired(true);

  var q2 = form.addMultipleChoiceItem()
    .setTitle('2. Lần gần nhất bạn mở slide của một buổi học trên LMS TRƯỚC KHI đến lớp là khi nào?')
    .setRequired(true);

  // ---- Phần 2: chỉ hiện với người đã từng xem slide ----
  var page2 = form.addPageBreakItem().setTitle('Lần gần nhất bạn xem trước slide');

  form.addTextItem()
    .setTitle('3. Trong 2 tuần qua, bạn đã xem trước slide trên LMS khoảng mấy buổi?')
    .setHelpText('Ghi một con số, vd 0, 2, 5')
    .setValidation(FormApp.createTextValidation().requireNumberBetween(0, 30).build())
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('4. Lần gần nhất đó, bạn có gặp chỗ nào trong slide mà bạn không hiểu không?')
    .setChoiceValues(['Không có', '1 chỗ', '2–3 chỗ', 'Nhiều hơn 3 chỗ'])
    .setRequired(true);

  form.addCheckboxItem()
    .setTitle('5. Với chỗ không hiểu đó, bạn đã làm gì? (chọn nhiều)')
    .setHelpText('Nếu câu 4 bạn chọn "Không có" thì chọn "Không gặp chỗ nào không hiểu"')
    .setChoiceValues(['Không gặp chỗ nào không hiểu', 'Đọc lại slide', 'Tra Google', 'Hỏi ChatGPT / Gemini riêng',
                      'Hỏi bạn', 'Hỏi trên Discord', 'Để dành hỏi trên lớp', 'Bỏ qua'])
    .showOtherOption(true)
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('6. Lần đó bạn mất khoảng bao lâu để hiểu ra (hoặc bỏ cuộc)?')
    .setChoiceValues(['Không gặp chỗ nào không hiểu', 'Dưới 5 phút', '5–15 phút', '15–30 phút', 'Trên 30 phút'])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('7. Cuối cùng bạn có hiểu được chỗ đó trước khi lên lớp không?')
    .setChoiceValues(['Không gặp chỗ nào không hiểu', 'Hiểu', 'Hiểu một phần', 'Không hiểu'])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('8. Nếu đã tra Google hoặc ChatGPT: câu trả lời có khớp với nội dung giảng viên giảng trên lớp không?')
    .setChoiceValues(['Khớp', 'Lệch một phần', 'Lệch nhiều', 'Không để ý / không tra'])
    .setRequired(true);

  // ---- Phần 3: mọi người ----
  var page3 = form.addPageBreakItem().setTitle('Câu cuối');

  form.addParagraphTextItem()
    .setTitle('9. Điều gì khó chịu nhất khi xem trước slide trên LMS? (kể một lần cụ thể nếu được)')
    .setHelpText('Đừng ghi tên người khác. Nhóm có thể trích nguyên văn câu này (ẩn danh) trong báo cáo.')
    .setRequired(false);

  form.addMultipleChoiceItem()
    .setTitle('10. Bạn có biết / có dùng trang pre-class (preclass-online.com, có video và khung chat hỏi trợ giảng AI) không?')
    .setChoiceValues(['Chưa từng nghe tới', 'Biết nhưng chưa dùng', 'Đã dùng 1–2 lần', 'Dùng thường xuyên'])
    .setRequired(true);

  form.addTextItem()
    .setTitle('11. (Tuỳ chọn) Nếu bạn sẵn lòng nhắn tin với nhóm 5 phút để kể thêm, để lại cách liên hệ:')
    .setRequired(false);

  // Nhánh ở câu 2: "Chưa bao giờ" → nhảy thẳng tới Phần 3
  q2.setChoices([
    q2.createChoice('Hôm nay', page2),
    q2.createChoice('Tuần này', page2),
    q2.createChoice('Tuần trước', page2),
    q2.createChoice('Lâu hơn', page2),
    q2.createChoice('Chưa bao giờ', page3)
  ]);

  // Sheet lưu kết quả
  var ss = SpreadsheetApp.create('Kết quả khảo sát slide LMS (BẢN GỐC — không commit)');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());

  Logger.log('Link GỬI cho mọi người: ' + form.getPublishedUrl());
  Logger.log('Link SỬA form:         ' + form.getEditUrl());
  Logger.log('Sheet kết quả:         ' + ss.getUrl());
}
