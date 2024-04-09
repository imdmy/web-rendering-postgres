struct TreeNode
{
	//! 子节点
	TreeNode *children[4];
	//! 包围盒
	glm::vec2 bMin, bMax;   //glm::vec2 是 glm 库中定义的一个数据类型，表示二维向量。在这里，bMin 和 bMax 分别是表示二维空间包围盒的最小和最大坐标的二维向量。
	//! 叶节点的物体列表
	std::vector<glm::vec2> objects;
	//! 是否是叶节点
	bool isLeaf;

	TreeNode() :
		isLeaf(false), bMin(glm::vec2(0.0f)), bMax(glm::vec2(0.0f))
	{
		children[0] = children[1] = children[2] = children[3] = nullptr;
	}

	TreeNode(glm::vec2 min, glm::vec2 max) :
		isLeaf(false), bMin(min), bMax(max)
	{
		children[0] = children[1] = children[2] = children[3] = nullptr;
	}
};

TreeNode * QuadTree::recursiveBuild(unsigned int depth, glm::vec2 min, glm::vec2 max,
	const std::vector<glm::vec2>& objects)
{
	//! if there is no object at all, just return nullptr.
	if (objects.empty())
		return nullptr;

	//! if the number of objects is less than 10 or reach the maxDepth,
	//! just create the node as leaf and return it.
	if (objects.size() < 4 || depth == mMaxDepth)
	{
		TreeNode *cur = new TreeNode(min, max);
		for (auto &point : objects)
		{
			if (isContain(point, min, max))
				cur->objects.push_back(point);
		}
		cur->isLeaf = true;
		return cur;
	}

	//! otherwise just subdivied into four sub nodes.
	glm::vec2 center = (min + max) * 0.5f;
	float length = std::max(max.x - min.x, max.y - min.y);

	// ---------
	// | 3 | 2 |
	// ---------
	// | 0 | 1 |
	// ---------
	glm::vec2 subMin[4];
	glm::vec2 subMax[4];

	//! get the four subnodes' region.
	subMin[0] = min;
	subMax[0] = center;
	subMin[1] = center - glm::vec2(0.0f, length / 2);
	subMax[1] = center + glm::vec2(length / 2, 0.0f);
	subMin[2] = center;
	subMax[2] = max;
	subMin[3] = min + glm::vec2(0.0f, length / 2);
	subMax[3] = center + glm::vec2(0.0f, length / 2);

	//! subdivide the objects into four classes according to their positions.
	std::vector<glm::vec2> classes[4];
	for (auto &point : objects)
	{s
		if (isContain(point, subMin[0], subMax[0]))
			classes[0].push_back(point);
		else if (isContain(point, subMin[1], subMax[1]))
			classes[1].push_back(point);
		else if (isContain(point, subMin[2], subMax[2]))
			classes[2].push_back(point);
		else if (isContain(point, subMin[3], subMax[3]))
			classes[3].push_back(point);
	}

	//! allocate memory for current node.
	TreeNode *cur = new TreeNode(min, max);
	cur->children[0] = recursiveBuild(depth + 1, subMin[0], subMax[0], classes[0]);
	cur->children[1] = recursiveBuild(depth + 1, subMin[1], subMax[1], classes[1]);
	cur->children[2] = recursiveBuild(depth + 1, subMin[2], subMax[2], classes[2]);
	cur->children[3] = recursiveBuild(depth + 1, subMin[3], subMax[3], classes[3]);

	return cur;
}