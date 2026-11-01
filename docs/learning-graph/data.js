// 学习图谱数据：由编者整理，概念与定义取自附录 D 术语表
// 改完后运行 python tools/graph_text.py，检查数据并更新 index.md 里的文字版
var CATS = ["示例类别一", "示例类别二"];
var CHAPTERS = ["", "语音技术概览", "声音与音频处理", "识别原理", "识别实战", "合成原理", "合成实战", "声纹与变声", "语音克隆", "应用与项目"];
var CHDIRS = ["", "01-overview", "02-audio", "03-asr-principles", "04-asr-practice", "05-tts-principles", "06-tts-practice", "07-speaker", "08-voice-cloning", "09-applications"];
var NODES = [
  {"id": "示例术语", "ch": 1, "cat": 0, "a": "g-示例术语", "d": "这里是术语表中的定义，鼠标悬停时显示"},
  {"id": "另一个术语", "ch": 1, "cat": 1, "a": "g-另一个术语", "d": "以示例术语为基础的概念"}
];
var EDGES = [["示例术语", "另一个术语"]];
