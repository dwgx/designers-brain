/* =============================================================================
   cues.js —— 单表双读（确定性契约 C6）：画面相位与音效卡点共用这一张表。
   画面（index.html）读 phases 决定「何时画/何时定格（升落/填色/文案）」；
   音频（audio.html）读 phases + sfx 决定合成事件时间。
   所有时间 = 帧号；帧号 / 30 = 秒。
   ============================================================================= */
"use strict";
window.CUES = {
  fps: 30,
  frames: 300,
  bpm: 120,                        // 15 帧/拍
  phases: [                        // 叙事相位（画面用；draw=true 表示「笔在画」）
    { name: "bike",  f0:   0, f1: 126, draw: true  },  // 自行车（后轮→车架→前轮）
    { name: "rays",  f0: 126, f1: 158, draw: true  },  // 前轮变成太阳（射线一笔甩出）
    { name: "rise",  f0: 158, f1: 182, draw: false },  // 太阳升起（定格，笔尖随太阳）
    { name: "ridge", f0: 182, f1: 216, draw: true  },  // 太阳落进山脊（画山脊）
    { name: "fall",  f0: 216, f1: 230, draw: false },  // 太阳落入山口（定格）
    { name: "badge", f0: 230, f1: 266, draw: true  },  // 山脊收拢成一枚徽章（闭环）
    { name: "fill",  f0: 266, f1: 284, draw: false },  // 闭合填色（从一点向外）
    { name: "text",  f0: 284, f1: 300, draw: false }   // 「山野骑行」
  ],
  sfx: [                           // 音效卡点（帧号 → 事件名；实现见 audio.html）
    { f:   0, name: "touch"      },  // 落笔
    { f: 126, name: "shimmerUp"  },  // 甩射线
    { f: 158, name: "riseGliss"  },  // 太阳升起
    { f: 182, name: "swell"      },  // 山脊起笔
    { f: 216, name: "fallGliss"  },  // 太阳下落
    { f: 230, name: "boom"       },  // 落入山口
    { f: 230, name: "whoosh"     },  // 徽章大回环
    { f: 266, name: "chime"      },  // 闭合
    { f: 266, name: "sparkle"    },  // 填色
    { f: 284, name: "chordEnd"   }   // 文案落定
  ]
};
