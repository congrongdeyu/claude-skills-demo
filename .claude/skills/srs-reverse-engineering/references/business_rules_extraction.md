# 业务规则提取指南

## 概述

业务规则是系统中的核心逻辑约束和操作规程。本指南介绍如何从代码中提取和识别业务规则。

## 业务规则分类

### 1. 验证规则 (Validation Rules)
**定义**: 确保输入数据符合特定格式和约束的规则

**代码模式识别**:
```javascript
// 字段长度验证
if (password.length < 8) {
    throw new Error("密码长度不能少于8位");
}

// 邮箱格式验证
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
if (!emailRegex.test(email)) {
    throw new Error("邮箱格式不正确");
}
```

```python
# 必填字段验证
if not email or not password:
    raise ValueError("邮箱和密码不能为空")

# 数值范围验证
if age < 18 or age > 120:
    raise ValueError("年龄必须在18-120之间")
```

**提取要点**:
- 输入验证条件
- 错误消息内容
- 验证的执行位置

### 2. 计算规则 (Calculation Rules)
**定义**: 涉及数值计算、公式应用的业务规则

**代码模式识别**:
```javascript
// 折扣计算
const discount = order.total >= 1000 ? 0.1 : 0.05;
const finalAmount = order.total * (1 - discount);

// 税费计算
const tax = amount * taxRate;
```

```python
# 积分计算
points = order_amount * conversion_rate

# 会员等级计算
if total_spent >= 10000:
    level = "VIP"
elif total_spent >= 5000:
    level = "GOLD"
else:
    level = "SILVER"
```

**提取要点**:
- 计算公式和算法
- 参与计算的数据项
- 计算结果的使用场景

### 3. 授权规则 (Authorization Rules)
**定义**: 控制用户访问权限和操作权限的规则

**代码模式识别**:
```java
// 角色权限检查
@PreAuthorize("hasRole('ADMIN')")
public void deleteUser(Long userId) {
    // 删除用户逻辑
}

// 资源所有权检查
if (!resource.getOwner().equals(currentUser)) {
    throw new AccessDeniedException("无权限访问此资源");
}
```

```python
# 权限装饰器
@admin_required
def delete_user(user_id):
    # 删除用户逻辑

# 条件权限检查
if user.role != 'manager' and not user.is_staff:
    return Response({'error': '权限不足'}, status=403)
```

**提取要点**:
- 权限检查条件
- 角色和权限定义
- 受保护的操作和资源

### 4. 业务流程规则 (Business Process Rules)
**定义**: 控制业务流程执行顺序和状态的规则

**代码模式识别**:
```javascript
// 订单状态流转
if (order.status === 'PENDING' && payment.success) {
    order.status = 'PAID';
    // 触发库存扣减
    inventory.reduce(order.items);
}

// 审批流程
if (amount > 10000) {
    // 需要经理审批
    await sendToManager(request);
} else if (amount > 1000) {
    // 主管审批
    await sendToSupervisor(request);
} else {
    // 自动批准
    approve(request);
}
```

```python
# 状态机模式
class OrderStatus:
    def next_status(self, order):
        if self.status == 'pending' and order.is_paid():
            return 'processing'
        elif self.status == 'processing' and order.is_shipped():
            return 'shipped'
        return self.status
```

**提取要点**:
- 状态转换条件
- 流程步骤和顺序
- 异常处理逻辑

### 5. 数据一致性规则 (Data Consistency Rules)
**定义**: 确保数据完整性和一致性的规则

**代码模式识别**:
```sql
-- 外键约束
ALTER TABLE orders ADD CONSTRAINT fk_user_id
FOREIGN KEY (user_id) REFERENCES users(id);

-- 唯一性约束
ALTER TABLE users ADD CONSTRAINT uk_email
UNIQUE (email);
```

```javascript
// 数据库事务
await transaction(async (trx) => {
    await trx('accounts').decrement('balance', amount)
        .where('id', from_account);
    await trx('accounts').increment('balance', amount)
        .where('id', to_account);
});
```

**提取要点**:
- 数据库约束条件
- 事务边界和操作
- 数据同步和一致性要求

## 规则提取方法论

### 1. 静态代码分析
**步骤**:
1. 识别规则相关关键词（validate, check, require, ensure等）
2. 分析条件语句和异常处理
3. 提取常量和配置值
4. 识别规则执行位置

### 2. 配置文件分析
**关注文件**:
- 数据库schema文件
- 验证规则配置文件
- 业务参数配置文件
- 权限配置文件

### 3. 测试用例分析
**价值**:
- 包含业务规则的预期行为
- 提供边界条件和异常情况
- 验证规则的正确性

## 规则文档化模板

### 验证规则模板
```
**规则编号**: VAL-[模块]-[序号]
**规则名称**: [规则简短名称]
**规则类型**: 验证规则
**触发条件**: [触发规则验证的条件]
**验证逻辑**: [详细的验证步骤]
**错误处理**: [验证失败的处理方式]
**业务含义**: [规则的业务目的]
**实现位置**: [代码文件和行号]
```

### 计算规则模板
```
**规则编号**: CAL-[模块]-[序号]
**规则名称**: [规则简短名称]
**规则类型**: 计算规则
**输入参数**: [参与计算的数据项]
**计算公式**: [具体的计算公式]
**精度要求**: [数值精度要求]
**业务含义**: [计算的业务意义]
**实现位置**: [代码文件和行号]
```

### 授权规则模板
```
**规则编号**: AUTH-[模块]-[序号]
**规则名称**: [规则简短名称]
**规则类型**: 授权规则
**适用对象**: [规则应用的用户或角色]
**权限条件**: [权限授予的条件]
**限制条件**: [权限限制的条件]
**违规处理**: [权限违规的处理方式]
**实现位置**: [代码文件和行号]
```

## 规则验证技术

### 1. 单元测试验证
- 为每个业务规则编写单元测试
- 覆盖正常情况和异常情况
- 验证边界条件

### 2. 集成测试验证
- 测试规则在业务流程中的执行
- 验证规则之间的相互作用
- 检查性能影响

### 3. 用户验收测试
- 验证规则符合业务需求
- 测试用户体验
- 确认异常处理

## 常见挑战和解决方案

### 挑战1: 规则分散在多个地方
**解决方案**:
- 建立规则注册表
- 使用规则引擎
- 统一规则管理

### 挑战2: 规则逻辑复杂
**解决方案**:
- 使用决策树
- 规则分解和组合
- 可视化规则表示

### 挑战3: 规则频繁变更
**解决方案**:
- 外部化规则配置
- 建立规则版本管理
- 实现热更新机制

## 工具和技术

### 规则引擎
- Drools (Java)
- Easy Rules (Java)
- business-rules-engine (Python)

### 文档工具
- 规则管理平台
- 协作文档系统
- 版本控制系统

### 测试工具
- 单元测试框架
- 规则测试工具
- 自动化测试平台

## 最佳实践

1. **规则命名规范**: 使用一致的命名约定
2. **规则分类管理**: 按功能模块和类型组织规则
3. **版本控制**: 跟踪规则的变更历史
4. **文档同步**: 保持代码和文档的同步
5. **定期审查**: 定期审查和更新规则文档
6. **性能监控**: 监控规则执行的性能影响

## 示例案例

### 电商订单验证规则
```
**规则编号**: VAL-ORDER-001
**规则名称**: 订单金额验证
**规则类型**: 验证规则
**触发条件**: 用户提交订单时
**验证逻辑**:
1. 订单总金额必须大于0
2. 订单总金额不能超过100万
3. 商品库存必须充足
**错误处理**: 返回具体的错误信息
**业务含义**: 防止无效订单和超卖
**实现位置**: services/order.js:45
```