# 非功能需求识别指南

## 概述

非功能需求（Non-Functional Requirements, NFR）描述了系统的质量属性和约束条件。本指南介绍如何从代码中识别和推断非功能需求。

## 非功能需求分类

### 1. 性能需求 (Performance Requirements)

#### 识别方法
**缓存机制检测**:
```javascript
// Redis缓存使用
const cache = redis.get(`user:${userId}`);
if (!cache) {
    const user = await database.getUser(userId);
    await redis.setex(`user:${userId}`, 300, JSON.stringify(user));
}
```
**推断**: 系统需要缓存热点数据以提高响应速度

**数据库优化**:
```sql
-- 索引创建
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_orders_user_id ON orders(user_id, created_at);
```
**推断**: 需要支持高效的查询性能

**异步处理**:
```python
# 异步任务处理
@celery.task
def send_email_async(user_id, message):
    # 发送邮件逻辑
    pass
```
**推断**: 需要处理耗时操作而不阻塞主流程

#### 文档化模板
```
**性能需求编号**: PERF-[序号]
**需求描述**: [具体性能要求]
**度量指标**: [可量化的指标]
**测试条件**: [测试环境和方法]
**代码证据**: [相关代码位置]
```

### 2. 安全性需求 (Security Requirements)

#### 识别方法
**身份认证**:
```java
// JWT认证
@PreAuthorize("isAuthenticated()")
public ResponseEntity<?> getUserProfile() {
    // 获取用户信息
}
```
**推断**: 系统需要用户身份认证机制

**权限控制**:
```python
# 角色权限检查
@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_panel(request):
    # 管理员面板逻辑
```
**推断**: 需要基于角色的访问控制

**输入验证**:
```javascript
// SQL注入防护
const query = 'SELECT * FROM users WHERE email = ?';
const result = db.query(query, [email]);
```
**推断**: 需要防止SQL注入等安全威胁

**数据加密**:
```python
# 密码哈希
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
```
**推断**: 敏感数据需要加密存储

#### 文档化模板
```
**安全需求编号**: SEC-[序号]
**需求描述**: [具体安全要求]
**威胁模型**: [防范的安全威胁]
**实现机制**: [安全实现方式]
**代码证据**: [相关代码位置]
```

### 3. 可靠性需求 (Reliability Requirements)

#### 识别方法
**错误处理**:
```javascript
try {
    const result = await riskyOperation();
    return result;
} catch (error) {
    logger.error('操作失败', error);
    throw new CustomError('服务暂时不可用');
}
```
**推断**: 系统需要具备错误恢复能力

**重试机制**:
```python
# 重试装饰器
@retry(max_attempts=3, delay=1)
def call_external_api():
    # 调用外部API
    pass
```
**推断**: 需要处理临时性故障

**数据备份**:
```bash
# 数据库备份脚本
#!/bin/bash
mysqldump -u root -p myapp > backup_$(date +%Y%m%d).sql
```
**推断**: 需要定期数据备份

**健康检查**:
```java
@RestController
public class HealthController {
    @GetMapping("/health")
    public ResponseEntity<String> health() {
        return ResponseEntity.ok("OK");
    }
}
```
**推断**: 需要系统健康监控

#### 文档化模板
```
**可靠性需求编号**: REL-[序号]
**需求描述**: [具体可靠性要求]
**故障场景**: [需要处理的故障类型]
**恢复策略**: [故障恢复方法]
**代码证据**: [相关代码位置]
```

### 4. 可扩展性需求 (Scalability Requirements)

#### 识别方法
**微服务架构**:
```yaml
# Docker Compose配置
services:
  user-service:
    image: user-service:latest
  order-service:
    image: order-service:latest
  payment-service:
    image: payment-service:latest
```
**推断**: 系统需要支持水平扩展

**负载均衡**:
```nginx
# Nginx负载均衡
upstream backend {
    server app1:3000;
    server app2:3000;
    server app3:3000;
}
```
**推断**: 需要支持负载均衡

**数据库分片**:
```python
# 数据库分片逻辑
def get_shard(user_id):
    return f"db_{user_id % 8}"
```
**推断**: 需要支持数据分片

**消息队列**:
```javascript
// 消息队列生产者
await queue.publish('order.created', {
    orderId: order.id,
    userId: order.userId
});
```
**推断**: 需要异步处理和系统解耦

#### 文档化模板
```
**可扩展性需求编号**: SCALE-[序号]
**需求描述**: [具体扩展性要求]
**扩展策略**: [扩展的实现方式]
**容量规划**: [预期的容量指标]
**代码证据**: [相关代码位置]
```

### 5. 可维护性需求 (Maintainability Requirements)

#### 识别方法
**日志记录**:
```python
import logging

logger = logging.getLogger(__name__)

def process_order(order):
    logger.info(f"处理订单 {order.id}")
    # 处理逻辑
    logger.info(f"订单 {order.id} 处理完成")
```
**推断**: 需要完善的日志记录机制

**配置外部化**:
```yaml
# application.yml
database:
  url: ${DB_URL:localhost}
  port: ${DB_PORT:5432}
```
**推断**: 需要配置的灵活管理

**模块化设计**:
```javascript
// 模块导出
module.exports = {
    UserService: require('./services/user-service'),
    OrderService: require('./services/order-service'),
    PaymentService: require('./services/payment-service')
};
```
**推断**: 需要模块化的代码结构

**API版本管理**:
```java
@RestController
@RequestMapping("/api/v1")
public class UserControllerV1 {
    // V1版本API
}

@RestController
@RequestMapping("/api/v2")
public class UserControllerV2 {
    // V2版本API
}
```
**推断**: 需要支持API版本演进

#### 文档化模板
```
**可维护性需求编号**: MAINT-[序号]
**需求描述**: [具体可维护性要求]
**实现方式**: [具体的实现策略]
**工具支持**: [使用的工具和框架]
**代码证据**: [相关代码位置]
```

### 6. 可用性需求 (Usability Requirements)

#### 识别方法
**国际化支持**:
```javascript
// i18n配置
import { useTranslation } from 'react-i18next';

function MyComponent() {
    const { t } = useTranslation();
    return <h1>{t('welcome')}</h1>;
}
```
**推断**: 需要多语言支持

**响应式设计**:
```css
/* 响应式CSS */
@media (max-width: 768px) {
    .container {
        padding: 10px;
    }
}
```
**推断**: 需要支持多种设备

**错误提示**:
```python
# 用户友好的错误信息
def validate_email(email):
    if not re.match(email_regex, email):
        raise ValidationError("请输入有效的邮箱地址")
```
**推断**: 需要用户友好的错误提示

#### 文档化模板
```
**可用性需求编号**: USAB-[序号]
**需求描述**: [具体可用性要求]
**用户群体**: [目标用户特征]
**使用场景**: [具体的使用场景]
**代码证据**: [相关代码位置]
```

## 识别方法论

### 1. 代码模式匹配
建立常见代码模式与非功能需求的映射关系：
- 缓存使用 → 性能需求
- 安全检查 → 安全需求
- 错误处理 → 可靠性需求
- 日志记录 → 可维护性需求

### 2. 配置文件分析
分析配置文件中的设置：
- 连接池配置 → 性能需求
- 超时设置 → 可靠性需求
- 安全配置 → 安全需求

### 3. 依赖库分析
分析项目依赖的库和框架：
- 使用Redis → 缓存性能需求
- 使用Spring Security → 安全需求
- 使用Prometheus → 监控需求

### 4. 架构模式识别
识别使用的架构模式：
- 微服务 → 可扩展性需求
- 事件驱动 → 可靠性需求
- 分层架构 → 可维护性需求

## 推断原则

### 1. 保守推断原则
当证据不足时，采用保守的推断：
- 不能确定性能要求时，标注"待确认"
- 推断结果要基于实际代码证据

### 2. 上下文相关原则
考虑项目的具体上下文：
- 企业内部系统可能有不同的安全要求
- 公网服务需要更高的可用性要求

### 3. 多证据支持原则
尽可能寻找多个证据支持推断：
- 代码实现 + 配置文件 + 依赖库
- 多个角度验证同一个需求

## 文档组织结构

### 按类别组织
```
## 5. 非功能需求

### 5.1 性能需求
- PERF-001: API响应时间要求
- PERF-002: 数据库查询性能要求

### 5.2 安全性需求
- SEC-001: 用户认证要求
- SEC-002: 数据加密要求

### 5.3 可靠性需求
- REL-001: 错误处理要求
- REL-002: 数据备份要求
```

### 按优先级组织
```
### 5.1 核心非功能需求
[必须满足的需求]

### 5.2 重要非功能需求
[应该满足的需求]

### 5.3 期望非功能需求
[可以满足的需求]
```

## 质量保证

### 1. 证据链完整性
确保每个需求都有相应的代码证据

### 2. 推断合理性
推断结果应该符合业务逻辑和技术现实

### 3. 可验证性
需求应该是可以通过测试验证的

### 4. 一致性
需求之间不应该有冲突

## 工具支持

### 代码分析工具
- 静态代码分析工具
- 依赖分析工具
- 复杂度分析工具

### 文档工具
- 需求管理工具
- 文档生成工具
- 协作平台

## 最佳实践

1. **证据驱动**: 基于实际代码证据进行推断
2. **渐进式分析**: 从明显需求开始，逐步深入
3. **多方验证**: 与开发人员讨论验证推断结果
4. **文档标注**: 明确标注推断的不确定性
5. **定期更新**: 随代码变更及时更新需求文档

## 常见误区

1. **过度推断**: 不要从少量代码推断过多需求
2. **忽略上下文**: 不考虑项目实际情况的推断
3. **缺乏证据**: 没有代码支持的纯推测
4. **一概而论**: 不考虑项目特殊性的通用推断
5. **忽视权衡**: 不考虑需求之间的权衡关系